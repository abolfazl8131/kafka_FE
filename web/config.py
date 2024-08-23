import os

config = {
    
    'kafka':{
        'host':os.environ.get('KAFKA_HOST'),
        'port':9092,
        'group-id':'kafka-stream',
        'topic':'AB123',
        'topic2':'vis'
    }
}