config = {
    
    'mongo': {
        'host':'localhost',
        'port':27017,
        'db':'test',
        'sparkuri':'mongodb://admin:admin@localhost:27017/test.test?authSource=admin'
    },
    'kafka':{
        'host':'localhost',
        'port':9092,
        'group-id':'kafka-stream',
        'topic':'AB123',
        'topic2':'vis'
    }
}