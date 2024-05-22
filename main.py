
import json
from kafka import KafkaConsumer
from src.config.environment import env

def start_application():
    
    consumer = KafkaConsumer(
            client_id=env.client_id,
            # bootstrap_servers='localhost:19092',
            bootstrap_servers=env.broker,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest'
            # auto_offset_reset='latest'
        )

    consumer.subscribe(env.topics.split(','))

    while True:
        raw_messages = consumer.poll(timeout_ms=100, max_records=200)
        for topic_partition, messages in raw_messages.items():
            for message in messages:
                print('@------MESSAGE------@~~~>')
                print(f'({topic_partition.partition}){topic_partition.topic}-> {message.value}')
                print('<~~~@------END-MESSAGE------@')


if __name__ == '__main__':
    start_application()