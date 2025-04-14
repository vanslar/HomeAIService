from flask import Blueprint, request
from CeleryTask.TaskLLMChat import Task_ChatResponse

LLMService_blueprint = Blueprint('LLMService', __name__)

@LLMService_blueprint.route('/ResponsePrompt', methods=['GET', 'POST'])
def ResponsePrompt():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = Task_ChatResponse.delay(prompt).get()
        return response 
    elif request.method == 'GET':
        prompt = "天为什么是蓝色的?" 
        response = Task_ChatResponse.delay(prompt).get()
        return response 
    return "HELLO"