import time 
from json import dumps  
from kafka import KafkaProducer  
from config import config
from ETL.Extract import create_response_dict
from ETL.transform import create_final_json


def get_producer():
    my_producer = KafkaProducer(  
        bootstrap_servers = [f'{config["kafka"]["host"]}:{config["kafka"]["port"]}'],  
        value_serializer = lambda x:dumps(x).encode('utf-8'), 
        api_version = (0, 10, 2)
        )
    return my_producer  


def start_streaming():

    producer = get_producer()
   
    while True:
        
        response_dict = create_response_dict()
        
        final_json = create_final_json(results=response_dict)
        producer.send(config['kafka']['topic'], final_json)
        time.sleep(1)


start_streaming()

