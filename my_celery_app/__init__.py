from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from celery.schedules import crontab
from datetime import datetime
today = datetime.now()

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryProject.settings')

app = Celery('my_celery_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.timezone = 'Asia/Karachi'
app.conf.enable_utc = True

app.conf.beat_schedule = {
    'run-every-day-at-3am': {
        'task': 'my_celery_app.tasks.add',  # task name
        'schedule': crontab(hour=11, minute=46),
        'args': (10, 10)  # arguments for the task
    },
}

app.conf.beat_schedule = {
    'sending_email': {
        'task': 'my_celery_app.tasks.sending_email',
        'schedule': crontab(hour=today.hour, minute=(today.minute + 2) % 60),
        'args': (),
        'options': {'expires': 60*60}
    },
}

print(app.conf.beat_schedule)
