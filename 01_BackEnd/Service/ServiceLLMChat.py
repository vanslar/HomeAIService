import lmstudio as lms
from config import SYSTEM_CONFIG

LLMClient = lms.llm(SYSTEM_CONFIG.LmsStudioModelName)

def ChatResponse(prompt):
    response = LLMClient.respond(prompt)
    return response