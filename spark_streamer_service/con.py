from json import loads  
from kafka import KafkaConsumer  
from config import config

def get_consumer(topic:str):
     my_consumer = KafkaConsumer(  
          topic,
          bootstrap_servers = [f'{config["kafka"]["host"]}:{config["kafka"]["port"]}'],  
          auto_offset_reset = 'earliest',  
          enable_auto_commit = True,  
          group_id = config['kafka']['group-id'],  
          value_deserializer = lambda x : loads(x.decode('utf-8')),
          api_version = (0, 10, 2) 
          )   
     return my_consumer


