#  Copyright (c) 2021.
#  Julio Cezar Riffel<julioriffel@gmail.com>

import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.update(
    task_annotations={
        'base.tasks.somar': {'rate_limit': '4/m'}
    }
)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'base.tasks.somar',
        'schedule': 10.0,
        'args': (16, 16)
    },
    'add-every-monday-morning': {
        'task': 'base.tasks.somar',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
app.conf.timezone = 'UTC'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
