from Service.ServiceLLMChat import ChatResponse
from . import CELERY_APP

@CELERY_APP.task
def Task_ChatResponse(prompt):
    response = ChatResponse(prompt)
    #LMStudioResponse的数据类型为 <class 'lmstudio.json_api.PredictionResult'>
    #因此需要转换
    return response