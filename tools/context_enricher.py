"""
Context Injection - Enriquece prompts dos agents com contexto SUPER DETALHADO do projeto
"""

from pathlib import Path
from typing import Optional
from tools.project_knowledge_base import get_knowledge_base
from tools.detailed_project_context import (
    PETAPI_STRUCTURE,
    PETSHOPWEBAPP_STRUCTURE,
    PETONAPP_STRUCTURE,
    SHARED_PATTERNS,
    ENVIRONMENTS,
)


class ContextEnricher:
    """
    Enriquece prompts e contextos com informações MUITO detalhadas:
    - Estrutura de pastas
    - Endpoints e APIs
    - Componentes
    - Models de dados
    - Padrões de código
    - Telas e fluxos
    """
    
    def __init__(self):
        self.kb = get_knowledge_base()
        self.detailed_contexts = {
            "pet.on.api": PETAPI_STRUCTURE,
            "petshop.webapp": PETSHOPWEBAPP_STRUCTURE,
            "pet.on.app": PETONAPP_STRUCTURE,
        }
    
    def _format_project_context(self, project_key: str) -> str:
        """Formata contexto super detalhado de um projeto"""
        if project_key not in self.detailed_contexts:
            return ""
        
        ctx = self.detailed_contexts[project_key]
        
        # Monta string com estrutura, endpoints, models, etc
        if "folder_structure" in ctx:
            folders = "\n".join([
                f"  - **{folder}**: {data.get('description', '')}" 
                for folder, data in ctx["folder_structure"].items()
            ])
        else:
            folders = ""
        
        formatted = f"""
╭─────────────────────────────────────────────────────────────────╮
│         CONTEXTO DETALHADO: {ctx['project'].upper()}
╰─────────────────────────────────────────────────────────────────╯

**Path**: {ctx.get('path', '')}
**Stack**: {ctx.get('stack', '')}
**Type**: {ctx.get('type', '')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 ESTRUTURA DE PASTAS:
{folders}

"""
        
        # Adiciona endpoints se existirem
        if "key_endpoints" in ctx:
            endpoints = ctx["key_endpoints"]
            if isinstance(endpoints, dict):
                endpoints_text = "\n".join([
                    f"  - {method}: {url} - {desc}"
                    for method, url, desc in [
                        (f"{m} {u}", u, desc) for m, u, desc in [item for sublist in [
                            [(k.split()[0], k.split()[1], v) for k, v in endpoint_dict.items()]
                            for endpoint_dict in endpoints.values()
                        ] for item in sublist]
                    ]
                ])
                formatted += f"🔌 PRINCIPAIS ENDPOINTS:\n{endpoints_text}\n\n"
        
        # Adiciona models se existirem
        if "models_database" in ctx:
            models_text = "\n".join([
                f"  - **{name}**: {data.get('fields', [])} → {data.get('relationships', [])}"
                for name, data in ctx["models_database"].items()
            ])
            formatted += f"💾 MODELOS DE DADOS:\n{models_text}\n\n"
        
        # Adiciona telas/features
        if "key_features" in ctx and isinstance(ctx["key_features"], dict):
            features_text = "\n".join([
                f"  - **{feat}**: {items}"
                for feat, items in ctx["key_features"].items()
            ])
            formatted += f"🎨 FUNCIONALIDADES:\n{features_text}\n\n"
        elif "screens" in str(ctx).lower():
            formatted += "🎨 TELAS\n"
        
        return formatted
    def enrich_planner_prompt(
        self,
        project_name: str,
        demand_type: str,
        title: str,
        description: str
    ) -> str:
        """
        Enriquece o prompt do Planner Agent com contexto SUPER DETALHADO
        """
        
        # Contexto básico da KB + contexto super detalhado
        project_context = self.kb.get_context_for_planner(project_name, demand_type)
        detailed_context = self._format_project_context(project_name.lower().replace(" ", "."))
        
        enriched = f"""
{project_context}

{detailed_context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 🎯 DEMANDA A PLANEJAR

**Título**: {title}
**Tipo**: {demand_type}
**Descrição**: 
{description}

---

## 📋 INSTRUÇÕES DE PLANEJAMENTO

Ao criar o plano você DEVE:

1. **Análise Inicial**
   - Qual é o impacto desta demanda?
   - Quais entidades de negócio são afetadas?
   - Há dependências com outros módulos/sistemas?
   - Como se integra com funcionalidades existentes?

2. **Análise Estrutural** 
   - Que pastas/arquivos serão modificados/criados?
   - Que endpoints podem ser afetados?
   - Que componentes precisam ser criados/modificados?

3. **Estruturação Técnica**
   - Decomponha em tarefas pequenas e testáveis
   - Cada tarefa deve resultar em uma mudança pequena e isolada
   - Identifique pontos de integração claros

4. **Critérios de Aceite CONCRETOS**
   - Comportamento esperado (o que deve acontecer)
   - Dados/inputs (com que dados testa)
   - Resultado (o que espera ver)
   - Validações que devem passar

5. **Tecnologias e Padrões**
   - Use EXATAMENTE os padrões consolidados no projeto
   - Reutilize componentes/classes existentes quando possível
   - Siga a arquitetura estabelecida (Controllers→Services→Repos)
   - Cite os arquivos que você conhece que existem

6. **Estimativa e Riscos**
   - Considere a complexidade de integração
   - Bugs/edge cases são comumente 30% do tempo
   - Liste riscos e como mitigá-los

## ✍️ FORMATO ESPERADO

Seu plano DEVE ser estruturado assim:

\`\`\`markdown
# Plano: [Título da Demanda]

## Resumo
[1-2 parágrafos explicando o que será feito, por que, e impacto]

## Análise de Impacto
- Entidades afetadas: [Listar]
- Endpoints envolvidos: [Listar]
- Arquivos a modificar: [Listar estrutura/arquivo.cs ou arquivo.vue]
- Componentes afetados: [Listar]

## Stack e Tecnologias
- [Tecnologia 1] para [o que]
- [Padrão a seguir] para [qual funcionalidade]

## Tarefas Técnicas

### 1. [Tarefa Específica]
- **Arquivo(s)**: src/Path/File.cs, src/Path/AnotherFile.ts
- **Descrição**: O que será feito com detalhe
- **Critérios de Aceite**:
  - ✓ Comportamento 1 com inputs específicos
  - ✓ Comportamento 2 com dados concretos
  - ✓ Integração com X funcionando

### 2. [Próxima Tarefa]
...

## Complexidade
Estimativa: Baixa / Média / Alta
Razão: [Especificar por que e quanto tempo]

## Riscos Identificados
- [Risco 1]: Impacto se falhar, Estratégia de mitigação
- [Risco 2]: ...

## Notas para o Developer
- Use padrão [Pattern] para [coisa]
- Cuidado especial com [edge case]
- Reutilize componente [ComponentName] que já existe em [path]
- Não esqueça de validar [campo] antes de usar
\`\`\`
"""
        
        return enriched
    
    def enrich_developer_prompt(
        self,
        project_name: str,
        title: str,
        description: str,
        plan: str
    ) -> str:
        """
        Enriquece o prompt do Developer Agent com contexto SUPER DETALHADO
        """
        
        dev_context = self.kb.get_context_for_developer(project_name)
        detailed_context = self._format_project_context(project_name.lower().replace(" ", "."))
        
        # Adiciona informações sobre padrões compartilhados
        patterns_info = f"""
🔐 PADRÕES COMPARTILHADOS NO PROJETO:

**Autenticação**: JWT Bearer Token
  - Tokens incluem: sub (userId), email, iat, exp
  - Enviados no header: Authorization: Bearer <token>

**Validação**: FluentValidation + Data Annotations
  - Exemplo: [Required], [StringLength], [Range], etc
  - Custom validators para regras de negócio

**Mapeamento**: AutoMapper para DTOs
  - Models → ViewModels para API
  - Use MapProfile classes para configurar

**Tratamento de Erros**: 
  - HTTP 400: Validation error com lista de errors
  - HTTP 401: Unauthorized
  - HTTP 404: Not Found
  - HTTP 500: Server error

**Formatos**: 
  - Datas: ISO 8601 (2024-03-20T15:30:00Z)
  - Valores decimais com ponto: 1.50 para R$1,50
  - Telefone: +55 (11) 98765-4321

**Regras de Negócio Chaves**:
  - Service minimum duration: 15 minutos
  - Agendamentos não podem se sobrepor mesmo pet
  - Cancelamento com 24h = reembolso total
  - Dados de pets LGPD compliant
"""
        
        enriched = f"""
{dev_context}

{detailed_context}

{patterns_info}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 💻 DEMANDA A IMPLEMENTAR

**Título**: {title}

**Descrição da demanda original**:
{description}

## 📋 Plano Aprovado pelo Planner
{plan}

---

## 🎯 INSTRUÇÕES DE IMPLEMENTAÇÃO

Você DEVE:

1. **Entenda o Plano COMPLETAMENTE**
   - Releia todas as tarefas
   - Entenda os critérios de aceite específicos
   - Saiba quais arquivos serão tocados
   - Verifique as dependências

2. **Antes de Começar**
   - Liste os arquivos que serão criados/modificados
   - Identifique componentes/classes existentes a reutilizar
   - Pense em todos os testes que precisará
   - Verifique se há validações que precisam ser feitas

3. **Durante a Implementação**
   - Escreva código LEGÍVEL com nomes descritivos
   - Siga EXATAMENTE os padrões do projeto (não invente novos)
   - Adicione comentários em lógca complexa (explicar por quê, não o quê)
   - Reutilize código existente - DRY (Don't Repeat Yourself)
   - Valide inputs/outputs apropriadamente
   - NUNCA ignore validações e regras de negócio

4. **Qualidade do Código**
   - Use async/await para operações I/O
   - Não deixe código morto ou comentado
   - Variáveis com nomes meaningfull
   - Máximo 5 parâmetros por função
   - Complexidade ciclomática < 10

5. **Estrutura Correta**
   - Controllers: Mapeiam HTTP requests → chamam Services
   - Services: Contêm lógica de negócio → chamam Repositories
   - Repositories: Acesso a dados → retornam Models
   - ViewModels: DTOs para requests/responses
   - Validação: Na entrada do Controller + camada de serviço

## 📝 FORMATO ESPERADO DA RESPOSTA

IMPORTANTE: Você PRECISA formatar assim para que o code extractor funcione:

```markdown
# Implementação: [Título]

## Resumo das Mudanças
- Arquivo 1: descrição
- Arquivo 2: descrição
- ...

## Código

# File: src/Services/NomeService.cs
\`\`\`csharp
using System;
using System.Threading.Tasks;
// ... imports necessários

namespace Pet.ON.Api.Services {{
    public class NomeService : INomeService {{
        // código aqui
    }}
}}
\`\`\`

# File: src/Controllers/NomeController.cs
\`\`\`csharp
// código aqui
\`\`\`

# File: src/ViewModels/NomeViewModel.cs
\`\`\`csharp
// código aqui
\`\`\`

[... mais arquivos com # File: header ...]

## Explicação Detalhada
- Por que essa abordagem?
- Como se integra com componentes existentes?
- Que padrões foram seguidos?

## Testes Recomendados
- Teste 1: Quando... espera...
- Teste 2: Quando... espera...
- Edge case: [situação especial]

## Como Testar Localmente
1. [Passo específico 1]
2. [Passo específico 2]

## Notas Importantes
- Depende de [funcionalidade] estar já implementada
- Use padrão [Pattern] porque [razão]
- Não esqueça de [verificação importante]
```

⚠️ CRÍTICOS PARA O CODE EXTRACTOR:
1. Use EXATAMENTE esse header: # File: src/path/to/NomeFile.cs
2. Cada bloco de código tem um \`\`\`csharp / \`\`\`typescript / etc
3. Sem comentários como "// File: ..." - use o header com #
4. Caminho COMPLETO: src/Services/NomeService.cs (não ./NomeService ou Services/NomeService)
"""
        
        return enriched
    
    def enrich_qa_prompt(
        self,
        project_name: str,
        title: str,
        plan: str,
        implementation: str
    ) -> str:
        """
        Enriquece o prompt do QA Agent com contexto SUPER DETALHADO
        """
        
        qa_context = self.kb.get_context_for_qa(project_name)
        detailed_context = self._format_project_context(project_name.lower().replace(" ", "."))
        
        enriched = f"""
{qa_context}

{detailed_context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ✅ REVISÃO DE QUALIDADE

**Demanda**: {title}

## 📋 Plano que foi Aprovado
{plan}

## 💻 Implementação Fornecida pelo Developer
{implementation}

---

## 🎯 INSTRUÇÕES DE ANÁLISE

Você está revisando código para qualidade, correção, segurança e padrões.

### 1. Verificação de Funcionalidade
- ✓ Implementação satisfaz TODOS os critérios de aceite do plano?
- ✓ Exemplos foram testados e funcionam?
- ✓ Há edge cases não tratados?
- ✓ A integração com componentes existentes está correta?
- ✓ Dependências foram declaradas corretamente?

### 2. Verificação de Arquitetura e Padrões
- ✓ Segue padrões do projeto (Controllers→Services→Repos)?
- ✓ Responsabilidades bem definidas (separation of concerns)?
- ✓ Sem duplicação de lógica (DRY)?
- ✓ Reutilizou componentes existentes quando possível?
- ✓ Nomes de classes/métodos são descritivos e seguem convenção?

### 3. Verificação de Validação
- ✓ Inputs são validados no Controller?
- ✓ Regras de negócio são verificadas no Service?
- ✓ Mensagens de erro são claras?
- ✓ Validação com FluentValidation foi usada?
- ✓ Data annotations (Required, StringLength, etc) corretos?

### 4. Verificação de Segurança
- ✓ Entradas são validadas contra injection attacks?
- ✓ Dados sensíveis são tratados apropriadamente?
- ✓ Não há hardecoded secrets/tokens?
- ✓ LGPD compliance checado (dados de usuários/pets)?
- ✓ Autenticação/autorização implementada?

### 5. Verificação de Performance
- ✓ N+1 query problems evitados (use Include para eager loading)?
- ✓ Índices de banco apropriados para queries?
- ✓ Caching implementado onde apropriado?
- ✓ Operações pesadas são async?
- ✓ Sem loops desnecessários ou complexidade O(n²)?

### 6. Verificação de Código
- ✓ Nomes são descritivos (não use i, x, temp)?
- ✓ Complexidade ciclomática < 10?
- ✓ Métodos têm máximo 5 parâmetros?
- ✓ Sem código morto ou comentado?
- ✓ Comentários explicam POR QUÊ, não O QUÊ?
- ✓ Consistência com resto do codebase?

### 7. Verificação de Testes
- ✓ Happy path é coberto?
- ✓ Edge cases importantes cobertos?
- ✓ Testes estão isolados (não dependem uns dos outros)?
- ✓ Mocks/stubs usados apropriadamente?
- ✓ Cobertura > 70%?

### 8. Verificação de Documentação
- ✓ Código é auto-documentado (clear intent)?
- ✓ Comentários em lógica complexa?
- ✓ Exemplos de uso fornecidos?
- ✓ Decisões arquiteturais explicadas?

## 📝 FORMATO DE RESPOSTA

estruture seu parecer EXATAMENTE assim:

\`\`\`markdown
# ✅ Análise de Qualidade: [Título]

## Veredicto
✅ Aprovado / ⚠️ Aprovado com Ressalvas / ❌ Reprovado

(Ser ⚠️ quer dizer que há problemas mas podem ser corrigidos antes de merge)
(Ser ❌ quer dizer que precisa ser replanejado/reimplementado)

## Resumo Executivo
[1-2 parágrafos sobre qualidade geral, aderência aos padrões, se resolve o problema]

## ✅ Pontos Positivos (Bem Feito)
- ✅ [Aspecto bem implementado e por quê]
- ✅ [Segue padrão X corretamente]
- ✅ [Bom tratamento de edge case]

## 🔴 Problemas Críticos
Impedem merge.

- **Problema 1**: [Descrição técnica clara]
  - Local: [arquivo, linha ou função afetada]
  - Impacto: [Por que é crítico - segurança, funcionalidade quebrada, etc]
  - Solução: [Como corrigir especificamente]

- **Problema 2**: [Outro crítico]
  - ...

## 🟡 Problemas Importantes
Devem ser corrigidos mas não bloqueiam merge imediato.

- **Problema 1**: [Descrição]
  - Solução: [Como melhorar]
  - Prioridade: Alta/Média

## 🔵 Sugestões de Melhoria
Não bloqueiam merge, mas melhoram qualidade.

- [Sugestão 1 com contexto]
- [Sugestão 2 com contexto]

## 🧪 Casos de Teste Obrigatórios
Estes DEVEM passar:
- Teste 1: [Cenário específico com inputs]
- Teste 2: [Edge case importante]
- Teste 3: [Integração com sistema existente]

## ✔️ Checklist Pré-Merge

- [ ] Todos críticos foram corrigidos
- [ ] Todos importantes foram corrigidos  
- [ ] Código segue padrões do projeto
- [ ] Testes passam
- [ ] Sem regressions

## Aprovação Final
- ✅ Pronto para merge into develop
- ⚠️ Pronto com condições (itens críticos/importantes fixados)
- ❌ Rejeitar e replanejar (muitos problemas ou arquitetura errada)

## Notas Adicionais
[Qualquer observação relevante]
\`\`\`

## ⚠️ Importante
- Seja rigorous - qualidade é responsabilidade sua
- Problemas encontrados agora custam 100x menos do que em produção
- Quando em dúvida, pera reviewar com lead tech
- Não deixe passar segurança, validação ou padrões
"""
        
        return enriched


# Singleton
_enricher = None


def get_context_enricher() -> ContextEnricher:
    """Retorna instância singleton"""
    global _enricher
    if _enricher is None:
        _enricher = ContextEnricher()
    return _enricher


if __name__ == "__main__":
    enricher = get_context_enricher()
    
    print("\n" + "="*70)
    print("ENRICHED PLANNER PROMPT")
    print("="*70)
    print(enricher.enrich_planner_prompt(
        "pet.on.api",
        "feature",
        "Adicionar suporte a fotos de capa para lojas",
        "As lojas precisam de uma foto de capa que apareça na listagem"
    ))
