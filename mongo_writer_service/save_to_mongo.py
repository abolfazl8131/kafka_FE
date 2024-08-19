from pymongo import MongoClient
from config import config
from con import get_consumer

def get_mongo_client():

    client = MongoClient(config['mongo']['host'], config['mongo']['port'])
    return client



def get_mongo_collection():
    client = get_mongo_client()
    col = client[config['mongo']['db']]['test']
    return col



def save_to_mongo():

    col = get_mongo_collection()

    my_consumer = get_consumer(config['kafka']['topic'])

    for message in my_consumer:  
        
        col.insert_one(message.value)

if __name__ == '__main__':

    save_to_mongo()