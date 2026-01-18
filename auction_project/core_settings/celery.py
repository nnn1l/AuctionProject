import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auction_project.settings")

app = Celery("auction_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "end-expired-auctions-every-minute": {
        "task": "auctions.tasks.end_expired_auctions",
        "schedule": crontab(minute="*"), # every 1 min
    },
}