# core/__init__.py

# Esta configuração garante que o app do Celery seja iniciado quando o Django iniciar.
try:
    from .celery import app as celery_app
except ModuleNotFoundError:
    # Ignora o erro se o Celery não estiver instalado (útil para momentos de build)
    pass
else:
    # Se a importação for bem-sucedida, define o __all__
    __all__ = ('celery_app',)