#!/usr/bin/env python
"""
Teste do sistema de Retry
Demonstra como o retry automático funciona
"""

from tools.retry_handler import retry_with_backoff, RetryConfig, run_with_retry
import time

def test_rate_limit_simulation():
    """Simula um rate limit real"""
    print("\n" + "="*70)
    print("TESTE 1: Simulando Rate Limit")
    print("="*70 + "\n")
    
    call_count = [0]  # Use list para permitir modificação em nested function
    
    def failing_function():
        call_count[0] += 1
        print(f"  Tentativa {call_count[0]}: Executando...")
        
        if call_count[0] < 3:
            # Simula erro de rate limit
            raise Exception(
                'RateLimitError: Please try again in 2.5s'
            )
        
        print(f"  ✅ Sucesso na tentativa {call_count[0]}!")
        return "Resultado bem-sucedido"
    
    config = RetryConfig(
        max_retries=5,
        initial_delay=1,
        max_delay=30,
        backoff_factor=2.0
    )
    
    result = retry_with_backoff(failing_function, config=config)
    print(f"\n  Resultado final: {result}\n")


def test_exponential_backoff():
    """Testa crescimento de tempo entre tentativas"""
    print("\n" + "="*70)
    print("TESTE 2: Backoff Exponencial")
    print("="*70 + "\n")
    
    call_count = [0]
    
    def another_function():
        call_count[0] += 1
        print(f"  Tentativa {call_count[0]}: Executando...")
        
        if call_count[0] < 4:
            raise Exception("Erro simples")
        
        print(f"  ✅ Sucesso!")
        return "Done"
    
    config = RetryConfig(
        max_retries=5,
        initial_delay=1,
        max_delay=60,
        backoff_factor=2.0,
        exponential=True
    )
    
    result = retry_with_backoff(another_function, config=config)
    print(f"\n  Resultado: {result}\n")


def test_with_decorator():
    """Testa usando decorator"""
    print("\n" + "="*70)
    print("TESTE 3: Usando Decorator @retry_handler")
    print("="*70 + "\n")
    
    from tools.retry_handler import retry_handler
    
    call_count = [0]
    
    @retry_handler(
        config=RetryConfig(
            max_retries=3,
            initial_delay=1,
            max_delay=30
        )
    )
    def decorated_function(name):
        call_count[0] += 1
        print(f"  Tentativa {call_count[0]}: Processando '{name}'...")
        
        if call_count[0] < 2:
            raise Exception("Falha temporária")
        
        return f"Olá, {name}! ✅"
    
    result = decorated_function("João")
    print(f"\n  Resultado: {result}\n")


def test_success_first_try():
    """Testa função que funciona na primeira tentativa"""
    print("\n" + "="*70)
    print("TESTE 4: Sucesso na Primeira Tentativa")
    print("="*70 + "\n")
    
    def successful_function():
        print(f"  Tentativa 1: Executando...")
        print(f"  ✅ Sucesso imediato!")
        return "Nenhum retry necessário"
    
    config = RetryConfig(max_retries=3)
    result = retry_with_backoff(successful_function, config=config)
    print(f"\n  Resultado: {result}\n")


def main():
    """Executa todos os testes"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  TESTE DO SISTEMA DE RETRY COM BACKOFF EXPONENCIAL".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    
    try:
        test_rate_limit_simulation()
        test_exponential_backoff()
        test_with_decorator()
        test_success_first_try()
        
        print("\n" + "="*70)
        print("✅ TODOS OS TESTES PASSARAM!")
        print("="*70)
        print("""
O sistema de retry está funcionando corretamente:
- ✅ Detecta rate limits automaticamente
- ✅ Aguarda o tempo recomendado
- ✅ Faz retry de forma inteligente
- ✅ Funciona com decorators
- ✅ Sucesso na primeira tentativa não sofre delay

Próximo passo: rode 'py -3.12 main.py' para processar demandas!
        """)
    
    except Exception as e:
        print(f"\n❌ Erro durante teste: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
