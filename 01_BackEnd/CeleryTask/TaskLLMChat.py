from Service.ServiceLLMChat import ChatResponse
from . import CELERY_APP

@CELERY_APP.task
def Task_ChatResponse(prompt):
    response = ChatResponse(prompt)
    return response