import os
import time

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dockerapp.settings')

app = Celery('service')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = settings.CELERY_BROKER_URL

app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print('Task executed')