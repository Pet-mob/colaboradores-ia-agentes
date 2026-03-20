"""
Sistema de Retry com Backoff Inteligente
Lida com rate limits do Groq e outras APIs automaticamente
"""

import time
import re
from typing import Callable, Any, TypeVar
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

T = TypeVar('T')


class RetryConfig:
    """Configuração de retry"""
    def __init__(
        self,
        max_retries: int = 5,
        initial_delay: int = 2,
        max_delay: int = 300,
        backoff_factor: float = 2.0,
        exponential: bool = True
    ):
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay
        self.backoff_factor = backoff_factor
        self.exponential = exponential


DEFAULT_RETRY_CONFIG = RetryConfig(
    max_retries=5,
    initial_delay=2,
    max_delay=300,
    backoff_factor=2.0,
    exponential=True
)


def _extract_retry_after(error_message: str) -> int | None:
    """
    Extrai o tempo de espera recomendado da mensagem de erro
    Retorna segundos, ou None se não encontrar
    """
    # Procura por "Please try again in 31.695s"
    match = re.search(r'try again in ([\d.]+)s', error_message)
    if match:
        return int(float(match.group(1))) + 2  # Adiciona 2s de margem
    
    # Procura por "Retry-After" header value
    match = re.search(r'Retry-After["\']?\s*:\s*(\d+)', error_message)
    if match:
        return int(match.group(1))
    
    return None


def retry_with_backoff(
    func: Callable[..., T],
    config: RetryConfig = DEFAULT_RETRY_CONFIG,
    error_types: tuple = (Exception,)
) -> T:
    """
    Executa função com retry automático e backoff exponencial
    
    Args:
        func: Função a executar
        config: Configuração de retry
        error_types: Tipos de erro para dar retry
    
    Returns:
        Resultado da função
    """
    
    attempt = 0
    delay = config.initial_delay
    
    while attempt <= config.max_retries:
        try:
            return func()
        
        except error_types as e:
            attempt += 1
            error_str = str(e)
            
            # Detecta rate limit específico
            is_rate_limit = any(phrase in error_str.lower() for phrase in [
                'rate limit',
                'rate_limit',
                '429',
                'too many requests',
                'quota'
            ])
            
            if attempt > config.max_retries:
                logger.error(f"❌ Falhou após {config.max_retries} tentativas")
                raise
            
            # Tenta extrair delay da própria resposta de erro
            retry_after = _extract_retry_after(error_str)
            
            if retry_after:
                wait_time = retry_after
                logger.warning(
                    f"⏳ Rate limit detectado! Aguardando {wait_time}s "
                    f"(conforme indicado pela API)"
                )
            elif is_rate_limit:
                wait_time = min(delay, config.max_delay)
                logger.warning(
                    f"⏳ Tentativa {attempt}/{config.max_retries} "
                    f"falhou com rate limit. "
                    f"Aguardando {wait_time}s antes de retry..."
                )
                delay = int(delay * config.backoff_factor) if config.exponential else delay
            else:
                # Para outros erros, retry mais rápido
                wait_time = min(delay, config.max_delay)
                logger.warning(
                    f"⚠️ Tentativa {attempt}/{config.max_retries} falhou: {e.__class__.__name__}. "
                    f"Aguardando {wait_time}s..."
                )
                delay = int(delay * config.backoff_factor) if config.exponential else delay
            
            time.sleep(wait_time)
    
    raise RuntimeError(f"Função falhou após {config.max_retries} tentativas")


def retry_handler(
    config: RetryConfig = DEFAULT_RETRY_CONFIG,
    error_types: tuple = (Exception,)
):
    """
    Decorator para retry automático
    
    Usage:
        @retry_handler(config=RetryConfig(max_retries=3))
        def my_function():
            return something()
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            return retry_with_backoff(
                lambda: func(*args, **kwargs),
                config=config,
                error_types=error_types
            )
        return wrapper
    return decorator


def run_with_retry(
    func: Callable[..., T],
    *args,
    max_retries: int = 5,
    initial_delay: int = 2,
    **kwargs
) -> T:
    """
    Função utilitária para rodar função com retry
    
    Usage:
        result = run_with_retry(
            my_function,
            arg1,
            kwarg1=value1,
            max_retries=3
        )
    """
    config = RetryConfig(
        max_retries=max_retries,
        initial_delay=initial_delay
    )
    
    return retry_with_backoff(
        lambda: func(*args, **kwargs),
        config=config,
        error_types=(Exception,)
    )


if __name__ == "__main__":
    # Teste simples
    import random
    
    call_count = 0
    
    def test_function():
        global call_count
        call_count += 1
        
        if call_count < 3:
            raise Exception(
                'RateLimitError: Please try again in 5.2s'
            )
        
        return "✅ Sucesso na tentativa " + str(call_count)
    
    result = retry_with_backoff(test_function)
    print(f"Resultado: {result}")
