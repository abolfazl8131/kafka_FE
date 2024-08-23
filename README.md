# About the project
This is a complete end-to-end data pipeline that supports real-time streaming and non-real-time analytics using different technologies such as MongoDB, Docker, Spark, Kafka, and also SQL.
here is a high-level implementation of it.

![Flowcharts](https://github.com/user-attachments/assets/40faeb40-4b97-4047-bf0b-7c622bace058)

Here you go! 

## How to run that?

simply first create 'venv' using this command

`python3 -m venv venv`

then is a time to install requirements for all services
I've put requirements in each service and the main folder, so you can activate the 'venv' and install requirements of the full pipeline.
`source venv/bin/activate && docker compose up`

easy! you've run some services like Kafka, MongoDB, and Zoo.

so you can open several terminals to run each service separately.

`python kafka_producer_service/pro.py`
`python mongo_writer_service/save_to_mongo.py`

