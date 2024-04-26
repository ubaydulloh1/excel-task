import os
import environ
from celery import Celery
from celery.schedules import crontab
from django.apps import apps
from django.conf import settings

env = environ.Env()
env.read_env(".env")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env.str("DJANGO_SETTINGS_MODULE"))

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.config_from_object(settings)
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app.conf.beat_schedule = {
    "update_products_task": {
        "task": "update_products_task",
        "schedule": crontab(minute=f"*/{settings.UPDATE_PRODUCTS_INTERVAL}"),
        'args': (),
    },
    "update_product_attributes_task": {
        "task": "update_products_task",
        "schedule": crontab(minute=f"*/{settings.UPDATE_PRODUCT_ATTRIBUTES_INTERVAL}"),
        'args': (),
    },

}
