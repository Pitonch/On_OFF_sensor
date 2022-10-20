from celery import Celery
import os
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'On_OFF_sensor.settings')
app = Celery('On_OFF_sensor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'каждую минуту': {
        'task': 'interaction.tasks.ping_sensor',
        'schedule': crontab(),
    },
}
