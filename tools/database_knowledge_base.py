"""
Database Knowledge Base para Pet.ON.Api
======================================

Documentação completa sobre:
- Schema do banco de dados
- Padrões Dapper específicos da Petmob
- Mapeamento entre colunas SQL e propriedades C#
- Retry patterns e error handling
- Stored procedures e queries complexas
- Enumerações e valores válidos
"""

# ============================================================================
# SCHEMA DO BANCO DE DADOS
# ============================================================================

DATABASE_SCHEMA = {
    "Usuario": {
        "description": "Usuários da plataforma (clientes e administradores)",
        "table": "Usuario",
        "columns": {
            "Id": {"type": "INT", "pk": True, "nullable": False},
            "Nome": {"type": "VARCHAR(255)", "nullable": False},
            "Email": {"type": "VARCHAR(255)", "nullable": True, "unique": True},
            "CNPJ": {"type": "VARCHAR(14)", "nullable": False, "unique": True},
            "Telefone": {"type": "VARCHAR(11)", "nullable": True},
            "Senha": {"type": "VARCHAR(255)", "nullable": False, "description": "Hash da senha, nunca texto plano"},
        },
        "relationships": {
            "Animal": "1:N",  # Um usuário tem muitos animais
            "Agendamento": "1:N",  # Um usuário faz muitos agendamentos
            "Endereco": "1:N",  # Um usuário tem múltiplos endereços
        }
    },
    
    "Animal": {
        "description": "Pets cadastrados pelos usuários",
        "table": "Animal",
        "columns": {
            "IdAnimal": {"type": "INT", "pk": True, "nullable": False},
            "IdUsuario": {"type": "INT", "fk": "Usuario.Id", "nullable": False},
            "Nome": {"type": "VARCHAR(100)", "nullable": False},
            "Raca": {"type": "VARCHAR(100)", "nullable": True},
            "Idade": {"type": "INT", "nullable": False, "range": [0, 30]},
            "Observacoes": {"type": "VARCHAR(500)", "nullable": True},
            "IdPorte": {"type": "INT", "nullable": False, "description": "Enum: 1=Pequeno, 2=Médio, 3=Grande"},
            "UrlFotoAnimal": {"type": "VARCHAR(500)", "nullable": True},
        },
        "relationships": {
            "Usuario": "N:1",  # Muitos animais para um usuário
            "Agendamento": "1:N",  # Um animal tem muitos agendamentos
        }
    },
    
    "Empresa": {
        "description": "PetShops (prestadores de serviço)",
        "table": "Empresa",
        "columns": {
            "IdEmpresa": {"type": "INT", "pk": True, "nullable": False},
            "DescricaoNomeFisica": {"type": "VARCHAR(255)", "nullable": False},
            "CNPJ": {"type": "VARCHAR(14)", "nullable": False, "unique": True},
            "Email": {"type": "VARCHAR(255)", "nullable": True},
            "Telefone": {"type": "VARCHAR(11)", "nullable": True},
            "IdCategoria": {"type": "INT", "fk": "Categoria.Id", "nullable": False},
            "Endereco": {"type": "VARCHAR(500)", "nullable": True},
            "UrlLogoEmpresa": {"type": "VARCHAR(500)", "nullable": True},
            "UrlCapaEmpresa": {"type": "VARCHAR(500)", "nullable": True},
        },
        "relationships": {
            "Servico": "1:N",  # Uma empresa oferece muitos serviços
            "Agendamento": "1:N",  # Uma empresa tem muitos agendamentos
            "HorariosFuncionamento": "1:N",  # Uma empresa tem múltiplos horários
        }
    },
    
    "Servico": {
        "description": "Serviços oferecidos pelo PetShop (banho, tosa, consulta, etc)",
        "table": "Servico",
        "columns": {
            "IdServico": {"type": "INT", "pk": True, "nullable": False},
            "IdEmpresa": {"type": "INT", "fk": "Empresa.IdEmpresa", "nullable": False},
            "Nome": {"type": "VARCHAR(200)", "nullable": False},
            "Descricao": {"type": "VARCHAR(1000)", "nullable": True},
            "Preco": {"type": "DECIMAL(10,2)", "nullable": False},
            "Duracao": {"type": "INT", "nullable": False, "description": "Duração em minutos"},
            "IdPorte": {"type": "INT", "nullable": True, "description": "Enum: NULL=Todos, 1-3=específico"},
            "IsAtivo": {"type": "BIT", "nullable": False, "default": 1},
        },
        "relationships": {
            "Empresa": "N:1",  # Muitos serviços para uma empresa
            "Agendamento": "1:N",  # Um serviço tem muitos agendamentos
            "SubServico": "1:N",  # Um serviço tem muitos sub-serviços
        }
    },
    
    "Agendamento": {
        "description": "Agendamentos de serviços",
        "table": "Agendamento",
        "columns": {
            "IdAgendamento": {"type": "INT", "pk": True, "nullable": False},
            "IdServico": {"type": "INT", "fk": "Servico.IdServico", "nullable": False},
            "IdAnimal": {"type": "INT", "fk": "Animal.IdAnimal", "nullable": False},
            "IdUsuario": {"type": "INT", "fk": "Usuario.Id", "nullable": False},
            "IdEmpresa": {"type": "INT", "fk": "Empresa.IdEmpresa", "nullable": False},
            "PacoteMensal": {"type": "BIT", "nullable": False, "default": 0},
            "Data": {"type": "DATETIME2", "nullable": False},
            "HorarioInicial": {"type": "TIME", "nullable": False},
            "HorarioFinal": {"type": "TIME", "nullable": False},
            "IdStatusAgendamento": {"type": "INT", "nullable": False, "description": "Enum: 1=Pendente, 2=Confirmado, 3=EmAtendimento, 4=Concluido, 5=Cancelado"},
            "IdAgendamentoPai": {"type": "INT", "fk": "Agendamento.IdAgendamento", "nullable": True, "description": "Para retorno de serviços"},
        },
        "relationships": {
            "Servico": "N:1",
            "Animal": "N:1",
            "Usuario": "N:1",
            "Empresa": "N:1",
        },
        "validations": {
            "HorarioFinal": "deve ser > HorarioInicial",
            "Data": "deve ser >= hoje",
        }
    },
    
    "HorariosFuncionamento": {
        "description": "Horários de funcionamento das empresas",
        "table": "horarios_funcionamento",
        "columns": {
            "IdEmpresa": {"type": "INT", "fk": "Empresa.IdEmpresa", "pk": True},
            "NomeDiaSemana": {"type": "VARCHAR(20)", "pk": True},
            "FuncionaNesseDia": {"type": "BIT", "nullable": False},
            "HorarioAbertura": {"type": "TIME", "nullable": True},
            "HorarioFechamento": {"type": "TIME", "nullable": True},
        }
    },
    
    "Endereco": {
        "description": "Endereços de usuários",
        "table": "Endereco",
        "columns": {
            "IdEndereco": {"type": "INT", "pk": True, "nullable": False},
            "IdUsuario": {"type": "INT", "fk": "Usuario.Id", "nullable": False},
            "Rua": {"type": "VARCHAR(255)", "nullable": False},
            "Numero": {"type": "VARCHAR(10)", "nullable": False},
            "Complemento": {"type": "VARCHAR(255)", "nullable": True},
            "Bairro": {"type": "VARCHAR(100)", "nullable": False},
            "Cidade": {"type": "VARCHAR(100)", "nullable": False},
            "Estado": {"type": "VARCHAR(2)", "nullable": False},
            "CEP": {"type": "VARCHAR(8)", "nullable": False},
            "Latitude": {"type": "DECIMAL(10,8)", "nullable": True},
            "Longitude": {"type": "DECIMAL(11,8)", "nullable": True},
        },
        "relationships": {
            "Usuario": "N:1",
        }
    }
}

# ============================================================================
# ENUMERAÇÕES E VALORES VÁLIDOS
# ============================================================================

ENUMS = {
    "PorteAnimal": {
        "1": "Pequeno",
        "2": "Médio", 
        "3": "Grande"
    },
    "StatusAgendamento": {
        "1": "Pendente",
        "2": "Confirmado",
        "3": "EmAtendimento",
        "4": "Concluido",
        "5": "Cancelado"
    },
    "DiaSemana": {
        "segunda-feira": "Monday",
        "terça-feira": "Tuesday",
        "quarta-feira": "Wednesday",
        "quinta-feira": "Thursday",
        "sexta-feira": "Friday",
        "sábado": "Saturday",
        "domingo": "Sunday"
    }
}

# ============================================================================
# PADRÕES DAPPER - COMO USAR NA API
# ============================================================================

DAPPER_PATTERNS = {
    "basic_query": """
// Padrão básico: Query simples
public async Task<Usuario> BuscarPorCNPJ(string cnpj)
{
    const string query = "SELECT Id, Telefone, CNPJ, Nome, Senha, Email FROM Usuario WHERE CNPJ = @CNPJ";
    
    return await SqlRetryHelper.ExecuteWithRetryAsync(() =>
        _dbConnection.QueryFirstOrDefaultAsync<Usuario>(
            query, 
            new { CNPJ = cnpj }
        )
    );
}
""",
    
    "query_with_parameters": """
// Padrão: Query com múltiplos parâmetros (POST body)
public async Task<IEnumerable<Usuario>> GetByParameters(BuscarUsuarioReqDto dto)
{
    var query = @"SELECT Id, Nome, CNPJ... FROM Usuario WHERE 1=1";
    var parameters = new DynamicParameters();
    
    if (!string.IsNullOrWhiteSpace(dto.CNPJ))
    {
        query += " AND CNPJ = @CNPJ";
        parameters.Add("CNPJ", dto.CNPJ);
    }
    
    if (dto.Id > 0)
    {
        query += " AND Id = @Id";
        parameters.Add("Id", dto.Id);
    }
    
    return await _dbConnection.QueryAsync<Usuario>(query, parameters);
}
""",

    "insert": """
// Padrão: INSERT com SCOPE_IDENTITY para retornar ID
public async Task<Usuario> InsertAsync(Usuario usuario)
{
    const string query = @"
        INSERT INTO Usuario (Nome, CNPJ, Telefone, Senha, Email)
        VALUES (@Nome, @CNPJ, @Telefone, @Senha, @Email);
        SELECT CAST(SCOPE_IDENTITY() as int)";
    
    var id = await _dbConnection.ExecuteScalarAsync<int>(query, usuario);
    usuario.Id = id;
    return usuario;
}
""",

    "update": """
// Padrão: UPDATE simples
public async Task<Usuario> UpdateAsync(Usuario usuario)
{
    const string query = @"
        UPDATE Usuario
        SET Nome = @Nome, Email = @Email, Telefone = @Telefone
        WHERE Id = @Id";
    
    await _dbConnection.ExecuteAsync(query, usuario);
    return usuario;
}
""",

    "transaction": """
// Padrão: Transação com múltiplas operações
public async Task AtualizarEmpresaComHorarios(Empresa empresa, List<HorariosFuncionamento> horarios)
{
    const string deleteQuery = @"DELETE FROM horarios_funcionamento WHERE id_empresa = @IdEmpresa";
    const string insertQuery = @"
        INSERT INTO horarios_funcionamento (id_empresa, nome_dia_semana, funciona_nesse_dia...)
        VALUES (@IdEmpresa, @NomeDiaSemana, @FuncionaNesseDia...)";
    
    if (_dbConnection.State == ConnectionState.Closed)
        _dbConnection.Open();
    
    using (var transaction = _dbConnection.BeginTransaction())
    {
        try
        {
            // Delete old records
            await _dbConnection.ExecuteAsync(deleteQuery, new { IdEmpresa = empresa.IdEmpresa }, transaction);
            
            // Insert new records
            foreach (var horario in horarios)
            {
                await _dbConnection.ExecuteAsync(insertQuery, horario, transaction);
            }
            
            transaction.Commit();
        }
        catch (Exception)
        {
            transaction.Rollback();
            throw;
        }
    }
}
""",

    "retry_pattern": """
// Padrão: Sempre usar SqlRetryHelper para operações críticas
private async Task<T> ExecuteComRetry<T>(Func<Task<T>> operacao)
{
    return await SqlRetryHelper.ExecuteWithRetryAsync(operacao);
}

// Uso:
var usuario = await ExecuteComRetry(() => 
    _dbConnection.QueryFirstOrDefaultAsync<Usuario>(query, parameters)
);
"""
}

# ============================================================================
# FIELD MAPPINGS - COLUNA SQL → PROPRIEDADE C#
# ============================================================================

FIELD_MAPPINGS = {
    "Usuario": {
        "Id": "Id",
        "CNPJ": "CNPJ",
        "Nome": "Nome",
        "Email": "Email",
        "Telefone": "Telefone",
        "Senha": "Senha",
    },
    "Animal": {
        "id_animal": "IdAnimal",
        "id_usuario": "IdUsuario",
        "nome": "Nome",
        "raca": "Raca",
        "idade": "Idade",
        "id_porte": "IdPorte",
        "observacoes": "Observacoes",
        "url_foto_animal": "UrlFotoAnimal",
    },
    "Empresa": {
        "id_empresa": "IdEmpresa",
        "fantasia_razao_social": "DescricaoNomeFisica",
        "CNPJ": "CNPJ",
        "Email": "Email",
        "Telefone": "Telefone",
        "id_categoria": "IdCategoria",
        "endereco": "Endereco",
        "url_logo_empresa": "UrlLogoEmpresa",
        "url_capa_empresa": "UrlCapaEmpresa",
    },
    "Servico": {
        "id_servico": "IdServico",
        "id_empresa": "IdEmpresa",
        "nome": "Nome",
        "descricao": "Descricao",
        "preco": "Preco",
        "duracao": "Duracao",
        "id_porte": "IdPorte",
        "is_ativo": "IsAtivo",
    },
    "Agendamento": {
        "id_agendamento": "IdAgendamento",
        "id_servico": "IdServico",
        "id_animal": "IdAnimal",
        "id_usuario": "IdUsuario",
        "id_empresa": "IdEmpresa",
        "pacote_mensal": "PacoteMensal",
        "data": "Data",
        "horario_inicial": "HorarioInicial",
        "horario_final": "HorarioFinal",
        "id_status_agendamento": "IdStatusAgendamento",
        "id_agendamento_pai": "IdAgendamentoPai",
    },
    "Endereco": {
        "id_endereco": "IdEndereco",
        "id_usuario": "IdUsuario",
        "rua": "Rua",
        "numero": "Numero",
        "complemento": "Complemento",
        "bairro": "Bairro",
        "cidade": "Cidade",
        "estado": "Estado",
        "cep": "CEP",
        "latitude": "Latitude",
        "longitude": "Longitude",
    }
}

# ============================================================================
# RETRY CONFIGURATION
# ============================================================================

SQL_RETRY_CONFIG = {
    "description": "Configuração de retry para erros transientes SQL Server",
    "transient_errors": [40613, 40197, 40501, 49918, 49919, 49920],
    "retry_count": 3,
    "exponential_backoff": "2^tentativa segundos",
    "usage": """
// SEMPRE use SqlRetryHelper para operações que podem ter erros transientes
public async Task<Usuario> BuscarPorCNPJ(string cnpj)
{
    return await SqlRetryHelper.ExecuteWithRetryAsync(() =>
        _dbConnection.QueryFirstOrDefaultAsync<Usuario>(query, new { CNPJ = cnpj })
    );
}
""",
    "helper_location": "Pet.ON.Infra/Helper/SqlRetryHelper.cs"
}

# ============================================================================
# STACK CONSTRAINTS - QUANDO NÃO USAR ENTITY FRAMEWORK
# ============================================================================

STACK_CONSTRAINTS = {
    "backend": {
        "orm": "Dapper (nunca Entity Framework)",
        "connection": "IDbConnection",
        "pattern": "Repository > Service > Controller",
        "validation": "FluentValidation",
        "dto_pattern": "Request/Response DTOs",
        "error_handling": "SqlRetryHelper para erros transientes",
        "namespaces": {
            "domain": "Pet.ON.Domain.Entidade",
            "dtos": "Pet.ON.Domain.Dtos",
            "repository": "Pet.ON.Infra.Repositorio",
            "service": "Pet.ON.Application.Servicos",
            "controller": "Pet.ON.Api.Controllers",
        },
        "forbidden": ["Entity Framework Core", "_context.Set<T>()", "DbSet<T>"],
        "required": ["Dapper", "IDbConnection", "DynamicParameters", "SqlRetryHelper"],
    }
}

# ============================================================================
# INSTRUÇÕES PARA AGENTS - CONTEXT INJECTION
# ============================================================================

def get_database_context_for_developer():
    """Retorna contexto para Developer Agent ao gerar código Backend"""
    return f"""
## ⚠️ IMPORTANTE: Stack Específico - Dapper, NÃO Entity Framework!

A API Pet.ON usa **DAPPER** para acesso a dados, não Entity Framework.

### Estrutura obrigatória para repositórios:

1. **Constructor com IDbConnection**
   private readonly IDbConnection _dbConnection;
   
2. **Raw SQL com Dapper**
   - QueryAsync<T>() para múltiplos registros
   - QueryFirstOrDefaultAsync<T>() para um registro
   - ExecuteAsync() para UPDATE/DELETE
   - ExecuteScalarAsync<T>() para INSERT com SCOPE_IDENTITY
   
3. **Sempre envolver em SqlRetryHelper**
   return await SqlRetryHelper.ExecuteWithRetryAsync(() => 
       _dbConnection.QueryFirstOrDefaultAsync<T>(...)
   );

4. **Field Mappings** - Banco usa snake_case, C# usa PascalCase:
   {FIELD_MAPPINGS}

5. **Exemplos de Padrões**:
   {DAPPER_PATTERNS['basic_query']}
   {DAPPER_PATTERNS['query_with_parameters']}
   {DAPPER_PATTERNS['transaction']}

### NÃO FAZER:
   ❌ _context.Set<T>()
   ❌ _context.Users.Where()
   ❌ Entity Framework queries
   ❌ LINQ to Entities
   
### FAZER:
   ✅ await _dbConnection.QueryAsync<T>(sql, parameters)
   ✅ using DynamicParameters para builds dinâmicos
   ✅ SqlRetryHelper.ExecuteWithRetryAsync(() => ...)
   ✅ Raw SQL com @NomeParametro
"""

def get_database_schema_summary():
    """Retorna resumo do schema para Quick Reference"""
    summary = "## Schema do Banco de Dados Pet.ON\n\n"
    for table, definition in DATABASE_SCHEMA.items():
        summary += f"### {table}\n"
        summary += f"{definition['description']}\n"
        summary += f"Table: `{definition.get('table', table)}`\n\n"
    return summary

if __name__ == "__main__":
    print(get_database_context_for_developer())
    print("\n" + "="*80 + "\n")
    print(get_database_schema_summary())
