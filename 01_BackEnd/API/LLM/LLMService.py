from flask import Blueprint, request
from CeleryTask.TaskLLMChat import Task_ChatResponse

LLMService_blueprint = Blueprint('LLMService', __name__)


@LLMService_blueprint.route('/Home')
def Home():
    return "LLMService Home"

@LLMService_blueprint.route('/ResponsePrompt', methods=['GET', 'POST'])
def ResponsePrompt():
    if request.method == 'POST':
        prompt = request.json['prompt']
        response = Task_ChatResponse.delay(prompt).get()
        return response 
    elif request.method == 'GET':
        prompt = "天为什么是蓝色的？"
        response = Task_ChatResponse.delay(prompt).get()
        return response 
    return "HELLO"


@LLMService_blueprint.route('/ChatTest', methods=['GET', 'POST'])
def ChatTest():
    if request.method == 'POST':
        print('BACKEND: POST')
        print( request.json)
        prompt = request.json['prompt']
        return 'POST TEST ' + prompt
    return "HELLO"