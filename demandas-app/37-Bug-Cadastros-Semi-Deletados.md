# Demanda #37: Bug - Cadastros Semi-Deletados

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Há um problema onde cadastros de usuários ou pets ficam em estado "semi-deletado" - não aparecem na interface do usuário mas deixam registros órfãos no banco de dados. Isso causa inconsistências de dados e problemas de referência.

### Impacto
- BD inconsistente
- Referências órfãs
- Possível causa de errors
- Dados fantasma

---

## 🎯 Critérios de Aceitação

- [ ] Deleção é completa (remove de todas as tabelas relacionadas)
- [ ] Não há registros órfãos deixados
- [ ] Sem registros "deleted_at" pendurados
- [ ] Agendamentos associados tratados:
  - [ ] Opção 1: Deletar também (se futuro)
  - [ ] Opção 2: Archive (manter histórico)
  - [ ] Opção 3: Notificar antes de deletar
- [ ] Soft deletes usados corretamente (se implementado)
- [ ] Queries filtram dados "deletados"
- [ ] Sem erros ao acessar/referenciar dados deletados

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Serviço de Usuários
- Serviço de Pets
- Banco de dados (lógica de deleção)
- Queries que referenciam dados

### Possíveis Causas
- Delete na tabela de usuário, mas não em pets/agendamentos
- Soft delete não implementado corretamente
- Cascade delete não configurado
- Múltiplos endpoints deletando parcialmente
- Transações não sendo usadas

### Solução Esperada
```sql
-- Usar transação
BEGIN TRANSACTION;
  DELETE FROM agendamentos WHERE petId IN (SELECT id FROM pets WHERE usuarioId = @userId);
  DELETE FROM pets WHERE usuarioId = @userId;
  DELETE FROM usuarios WHERE id = @userId;
COMMIT;

-- OU usar soft delete
UPDATE usuarios SET deletedAt = GETDATE(), ativo = 0 WHERE id = @userId;
-- E filtrar em queries: WHERE ativo = 1 AND deletedAt IS NULL
```

---

## 📊 Estimativa

- **Esforço:** Médio-Grande (2-3 dias)
- **Complexidade:** Média-Alta
- **Prioridade:** Alta

---

## 🔗 Dependências

- Acesso ao banco de dados
- Coordenação com backend

---

## 📝 Checklist de Resolução

- [ ] Mapear tabelas relacionadas
- [ ] Decidir: hard delete vs soft delete
- [ ] Implementar transações
- [ ] Adicionar cascade delete (se hard delete)
- [ ] Adicionar soft delete fields (se soft delete)
- [ ] Atualizar queries para filtrar deleted records
- [ ] Testar deleção de usuário com pets/agendamentos
- [ ] Verificar BD após testes
- [ ] Limpeza manual de registros órfãos existentes (se necessário)
