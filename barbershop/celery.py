import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barbershop.settings')

app = Celery('barbershop')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'send-notification-every-day-breakfast': {
        'task': 'diets.tasks.send_sms_breakfast',
        'schedule': crontab(minute='*/15', hour='14'),
    },
    'send-notification-every-day-lunch': {
        'task': 'diets.tasks.send_sms_lunch',
        'schedule': crontab(minute='*/15',
                            hour=19
                            ),
    },
    'send-notification-every-day-dinner': {
        'task': 'diets.tasks.send_sms_lunch',
        'schedule': crontab(minute='*/15',
                            hour=19
                            ),
    }
}

app.autodiscover_tasks()