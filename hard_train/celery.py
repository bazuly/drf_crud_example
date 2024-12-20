from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hard_train.settings')


app = Celery('hard_train')

app.conf.broker_url = 'amqp://guest:guest@rabbitmq:5672/'
app.conf.result_backend = 'redis://redis:6379/0'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
