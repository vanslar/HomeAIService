from flask import Flask, blueprints
from flask_cors import CORS
from API.LLM.LLMService import LLMService_blueprint

FLASK_APP = Flask(__name__)
CORS(FLASK_APP)

FLASK_APP.register_blueprint(
            LLMService_blueprint,
            url_prefix='/LLMService'
            #static_folder='static',
            #template_folder='templates'
)

if __name__ == '__main__':
    FLASK_APP.run(host='0.0.0.0', port=5001)
