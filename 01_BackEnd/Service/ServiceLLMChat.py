import lmstudio as lms
from config import SYSTEM_CONFIG

lms.get_default_client(SYSTEM_CONFIG.LmsStudioServerHost)

LLMClient = lms.llm(SYSTEM_CONFIG.LmsStudioModelName)
def ChatResponse(prompt):
    response = LLMClient.respond(prompt)
    #LMStudioResponse的数据类型为 <class 'lmstudio.json_api.PredictionResult'>
    #因此需要转换
    return response.content