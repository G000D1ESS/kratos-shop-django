from suit.apps import DjangoSuitConfig

from celery import Celery

celery_app = Celery('proj')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
