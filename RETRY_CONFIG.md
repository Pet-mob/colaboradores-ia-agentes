# Configuração de Retry automático

## O que foi implementado

Adicionamos um **sistema automático de retry com backoff exponencial** que:

1. **Detecta Rate Limit** - Identifica quando a API Groq atingiu limite
2. **Aguarda automaticamente** - Não falha imediatamente, espera o tempo necessário
3. **Tenta novamente** - Executa novamente após aguardar
4. **Exponential Backoff** - A cada falha, aguarda mais tempo (2s → 4s → 8s → ...)

## Como funciona

Quando o `crew.kickoff()` falha com rate limit:

```
Tentativa 1: Executa → Rate Limit → Aguarda 2s
Tentativa 2: Executa → Rate Limit → Aguarda 4s
Tentativa 3: Executa → Rate Limit → Aguarda 8s
Tentativa 4: Executa → Rate Limit → Aguarda 16s
Tentativa 5: Executa → ✅ Sucesso!
```

## Customizando Retry

### Aumentar número de tentativas

Edite [agents/orchestrator.py](agents/orchestrator.py):

```python
retry_config = RetryConfig(
    max_retries=10,  # Aumentar para 10 tentativas
    initial_delay=2,
    max_delay=300,
    backoff_factor=2.0
)
```

### Mudar estratégia de backoff

```python
# Mais agressivo
retry_config = RetryConfig(
    max_retries=5,
    initial_delay=1,      # Come
ça com 1s
    max_delay=60,         # Max 60s
    backoff_factor=1.5    # Cresce menos rápido
)

# Mais conservador
retry_config = RetryConfig(
    max_retries=3,
    initial_delay=5,      # Começa com 5s
    max_delay=600,        # Max 10min
    backoff_factor=3.0    # Cresce mais rápido
)
```

## Como usar em outros lugares

### Como decorator

```python
from tools.retry_handler import retry_handler, RetryConfig

@retry_handler(max_retries=3)
def minha_funcao():
    # seu código aqui
    pass

resultado = minha_funcao()  # Retry automático se falhar
```

### Como função utilitária

```python
from tools.retry_handler import run_with_retry

resultado = run_with_retry(
    minha_funcao,
    arg1,
    kwarg1=value,
    max_retries=5
)
```

## Arquivos modificados

- ✅ **tools/retry_handler.py** - Novo módulo com sistema de retry
- ✅ **agents/orchestrator.py** - Integração do retry com crew.kickoff()

## Próxima vez que rodar

```bash
py -3.12 main.py
```

Se atingir rate limit novamente, o sistema vai:

- ✅ Aguardar automaticamente
- ✅ Fazer retry sem intervenção
- ✅ Exibir progresso das tentativas

## Detecção Automática de Delay

O sistema também **lê a mensagem de erro** para extrair o tempo recomendado:

```
❌ Erro: "Please try again in 31.695s"
✅ Sistema detecta → Aguarda 31.7s
✅ Tenta novamente automaticamente
```

Isso torna o retry ainda mais eficiente! 🚀
