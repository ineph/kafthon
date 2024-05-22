import json
from kafka import KafkaConsumer
from src.config.environment import env


class Konsumer:
    def __init__(self) -> None:
        a = env.topics
        print('sdadsd')
        self.consumer = KafkaConsumer(
            # f'{env.topics}',
            client_id=env.client_id,
            # bootstrap_servers='localhost:19092',
            bootstrap_servers=env.broker,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest'
            # auto_offset_reset='latest'
)
        
consumer = Konsumer()