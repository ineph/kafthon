import os

class Environment:
    def __init__(self) -> None:

        self._KAFKA_BROKER = os.getenv('KAFKA_BROKER')
        self._CLIENT_ID = os.getenv('CLIENT_ID')
        self._TOPICS = os.getenv('TOPICS','')


    @property
    def broker(self):
        return self._KAFKA_BROKER
    
    @property
    def client_id(self):
        return self._CLIENT_ID
    
    @property
    def topics(self):
        return self._TOPICS

env = Environment()