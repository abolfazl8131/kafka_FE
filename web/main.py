from fastapi import FastAPI
from config import config
import asyncio
from fastapi.templating import Jinja2Templates
import ast
from aiokafka import AIOKafkaConsumer

app = FastAPI()


async def consume():
    consumer = AIOKafkaConsumer(config['kafka']['topic2'],
                                bootstrap_servers=f'{config["kafka"]["host"]}: {config["kafka"]["port"]}')
    
    await consumer.start()
    try:
        async for msg in consumer:

            my_string = msg.value.decode("utf-8")
            my_dict = ast.literal_eval(my_string)
            my_dict = tuple(my_dict)
            lat = my_dict[0]
            long = my_dict[1]
            data = {
                'lat':lat,
                'long':long
            }
            print(data)
           
    finally:
        await consumer.stop()


asyncio.create_task(consume())