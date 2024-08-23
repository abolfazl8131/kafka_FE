import os
config = {
    
    'mongo': {
        'host':os.environ.get('MONGO_HOST'),
        'port':27017,
        'db':os.environ.get('DB'),
        'uri':os.environ.get('CONNECTION_URL')
    },
  
}