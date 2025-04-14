import lmstudio as lms
from config import SYSTEM_CONFIG

lms.get_default_client(SYSTEM_CONFIG.LmsStudioServerHost)

LLMClient = lms.llm(SYSTEM_CONFIG.LmsStudioModelName)
def ChatResponse(prompt):
    response = LLMClient.respond(prompt)
    return response