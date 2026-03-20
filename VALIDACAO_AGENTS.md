# Guia de Validação dos Agents

## Problema

Os agents estão "perdidos" porque não há um mecanismo claro de validação que mostra:

1. Se cada agent produziu um output significativo
2. Se o output contém as informações esperadas
3. Se houve mudanças reais no repositório

## Solução

Criamos um sistema de **validação automática** que:

### ✅ Valida Outputs dos Agents

Para cada agent, o validador verifica:

- **Tamanho do output**: Detecta outputs muito curtos (empty ou insignificantes)
- **Conteúdo esperado**: Verifica se contém elementos necessários

  **Planner Agent deve conter:**
  - Tarefas/passos técnicos
  - Critérios de aceite
  - Tecnologias/stack

  **Developer Agent deve conter:**
  - Blocos de código (`código`)
  - Classes, funções ou estruturas
  - Explicações técnicas

  **QA Agent deve conter:**
  - Problemas/bugs encontrados
  - Veredicto final (✅/⚠️/❌)
  - Sugestões de melhoria

- **Detecção de alucinações**: Identifica quando o LLM diz "não tenho acesso" ou "não posso"
- **Score de qualidade**: Cada agent recebe uma nota de 0-100

### 📊 Rastreia Mudanças Git

- Monitora arquivos modificados na branch da demanda
- Conta linhas de código adicionadas
- Valida se houve commits reais

### 📋 Gera Relatório Visual

Ao final de cada demanda, você vê:

```
======================================================================
RELATÓRIO DE VALIDAÇÃO - 044-bug-dados-incorretos
======================================================================

✅ PLANNER          | Score: 85/100  | Output: 1500 chars
✅ DEVELOPER        | Score: 92/100  | Output: 3200 chars
⚠️ QA               | Score: 45/100  | Output: 800 chars
   ⚠️ QA Report faltando: veredicto

📝 Mudanças no Git:
   • src/Services/PetService.cs: +150 linhas
   • tests/PetServiceTests.cs: +80 linhas
   Total: 230 linhas modificadas

======================================================================
✅ EXECUÇÃO BEM-SUCEDIDA
======================================================================
```

## Como Usar

### 1️⃣ Validação Automática (Durante Execução)

A validação acontece **automaticamente** ao final de cada demanda:

```bash
py -3.12 main.py
# ... agents executam ...
# ... validação aparece automaticamente ...
```

### 2️⃣ Validação Manual (Debug)

Para testar validação sem rodar toda a pipeline:

```bash
# Menu interativo
py -3.12 validate_agents.py

# Validar arquivo específico
py -3.12 validate_agents.py demands/in_progress/044-bug-dados-incorretos.md
```

O script oferece opções:

- Validar output individual de um agent
- Validar demanda completa (arquivo .md)
- Testar com dados de exemplo

## Interpretando os Resultados

### Score de Qualidade

| Score  | Status       | Significa                           |
| ------ | ------------ | ----------------------------------- |
| 80-100 | ✅ Excelente | Output útil e completo              |
| 60-79  | ✅ Bom       | Output válido com poucas ressalvas  |
| 40-59  | ⚠️ Aceitável | Output com problemas significativos |
| 0-39   | ❌ Inválido  | Output inútil ou muito curto        |

### Problemas Comuns

| Problema                             | Causa                      | Solução                      |
| ------------------------------------ | -------------------------- | ---------------------------- |
| "Output muito curto"                 | Agent não produziu nada    | Verificar prompt/contexto    |
| "Output contém menção de erro"       | Erro durante execução      | Ver logs do agent            |
| "Output contém limitações do modelo" | Alucinação do LLM          | Melhorar instruções          |
| "Plano faltando: tarefas"            | Planner não estruturou bem | Revisar prompt do Planner    |
| "Nenhum bloco de código encontrado"  | Developer não gerou código | Melhorar contexto/instruções |
| "QA Report faltando: veredicto"      | QA não concluiu análise    | Aumentar output_tokens       |

## Estrutura do Código

### `tools/agents_validator.py`

Módulo principal com:

- `ValidationResult`: Dataclass com resultado de validação
- `ExecutionReport`: Dataclass com relatório completo
- `validate_agent_output()`: Valida output individual
- `generate_validation_report()`: Gera relatório completo
- `print_validation_report()`: Exibe relatório formatado

### `validate_agents.py`

Script de CLI com:

- Menu interativo
- Validação de arquivo individual
- Testes com dados de exemplo

### `agents/orchestrator.py` (modificado)

Agora chama validador ao final da execução.

## Próximos Passos para Melhorar

### 1. Aumentar Verbosidade

Os agents precisam saber exatamente o que espera-se deles. Considere:

- Adicionar exemplos de output esperado nos prompts
- Incluir "Formato esperado:" nas descrições das tasks

### 2. Validação Contextual

Adicionar validação que entende o domínio:

- Verificar se código está correto sintaticamente
- Validar se testes cobrem casos de uso
- Análise de segurança automática

### 3. Feedback Loop

Implementar loop de melhoria:

- Se score < 50, fazer retry com prompt ajustado
- Se git_changes == 0, alertar que agents não implementaram nada

### 4. Métricas

Rastrear métricas ao longo do tempo:

- Score médio por agent
- Taxa de sucesso por tipo de demanda
- Tempo médio de execução

## Debug - Checklist

Se os agents estão "perdidos", verifique:

- [ ] LLM está funcionando? (verificar chave API)
- [ ] Tasks têm descrição clara? (em `dev_tasks.py`)
- [ ] Context das tasks é suficiente? (agents conseguem entender?)
- [ ] Output do agent está sendo capturado? (verificar `orchestrator.py`)
- [ ] Arquivo .md está sendo atualizado? (verificar `queue_manager.py`)
- [ ] Git tem as mudanças? (rodar `git diff` manually)

## Exemplos

### ✅ Execução Bem-Sucedida

```
✅ PLANNER          | Score: 88/100
✅ DEVELOPER        | Score: 92/100
✅ QA               | Score: 85/100

📝 Mudanças no Git:
   • src/Controllers/PetController.cs: +200 linhas
   • tests/PetControllerTests.cs: +150 linhas
   Total: 350 linhas modificadas

✅ EXECUÇÃO BEM-SUCEDIDA
```

### ⚠️ Execução com Ressalvas

```
✅ PLANNER          | Score: 80/100
⚠️ DEVELOPER        | Score: 45/100
   ⚠️ Poucos blocos de código: 1
   ⚠️ Output muito curto (800 chars)
✅ QA               | Score: 75/100

❌ Nenhuma mudança detectada no Git

⚠️ AGENTS PRODUZIRAM OUTPUT, MAS SEM MUDANÇAS GIT
```

Os agents geraram plano e análise, mas o Developer não implementou nada real.

### ❌ Execução Falhada

```
❌ PLANNER          | Score: 25/100
   ⚠️ Output muito curto (100 chars)
   ⚠️ Plano faltando: tarefas
   ⚠️ Plano faltando: critérios
❌ DEVELOPER        | Score: 0/100
   ⚠️ Output muito curto (50 chars)

❌ EXECUÇÃO COM PROBLEMAS
```

Algo deu muito errado - verifique logs e chave API.
