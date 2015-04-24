from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from settings import Config

celery = Celery('tasks',broker=Config.BROKER_URL)


@periodic_task(run_every=timedelta(hours=5))
def mytask():
    pass