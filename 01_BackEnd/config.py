import os

class Config:
    LmsStudioServerHost = 'localhost:1234'
    LmsStudioModelName = 'deepseek-r1-distill-qwen-7b'
    #LmsStudioModelName = 'deepseek-r1-distill-qwen-1.5b'

class DevelopmentConfig(Config):
    DEBUG = True
    RedisHost = 'localhost'


class DockerConfig(Config):
    DEBUG = False
    RedisHost = 'redis'

if os.getenv('HOME_AI_SERVICE') == None:
    SYSTEM_CONFIG = DevelopmentConfig()
elif os.getenv('HOME_AI_SERVICE') == 'HOME_SERVICE_DOCKER':
    SYSTEM_CONFIG = DockerConfig()
else:
    SYSTEM_CONFIG = DevelopmentConfig()
