from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hard_train.settings')


app = Celery('hard_train', backend='redis://6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
