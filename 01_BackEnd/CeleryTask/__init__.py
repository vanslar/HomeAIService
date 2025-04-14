from celery import Celery
from config import SYSTEM_CONFIG
CELERY_APP = Celery(
        'celery_app', 
        broker=f'redis://{SYSTEM_CONFIG.RedisHost}:6379/0', 
        backend=f'redis://{SYSTEM_CONFIG.RedisHost}:6379/1',
        include=[
                'CeleryTask.TaskLLMChat'
                ]
    )