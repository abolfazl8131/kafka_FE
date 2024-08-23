import os

config = {
    
    'mongo': {
        'host':os.environ.get('MONGO_HOST'),
        'port':27017,
        'db':os.environ.get('DB'),
        'uri':os.environ.get('CONNECTION_URL')
    },
     'kafka':{
        'host':os.environ.get('KAFKA_HOST'),
        'port':9092,
        'group-id':'kafka-stream',
        'topic':'AB123',
        'topic2':'vis'
    }
}