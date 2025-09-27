import os
from celery import Celery

# Configura o Django settings module para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usa uma string para que o worker não tenha que serializar
# o objeto de configuração para processos filhos
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega tarefas de todos os apps registrados
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

