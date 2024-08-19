from config import config
from pyspark.sql import SparkSession
import os
from pyspark.sql.functions import col
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType,StructField

schema = StructType([
    StructField("latitude", StringType()),
    StructField("longitude", StringType())
])

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.2,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2 pyspark-shell'

# Create SparkSession
spark = SparkSession.builder.appName("RealTimeProcessing").getOrCreate()

# Read real-time data from a Kafka topic
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", f'{config["kafka"]["host"]}:{config["kafka"]["port"]}') \
    .option("subscribe", config['kafka']['topic']) \
    .option("startingOffsets", "latest") \
    .option("includeHeaders", "true") \
    .option("failOnDataLoss", "false") \
    .load()

#Apply real-time transformations or analytics
my_df = df.selectExpr("CAST(value AS STRING) as json")
clean_df = my_df.select(from_json(col("json").cast("string"), schema).alias("value")).selectExpr("CAST(value AS STRING) as value")


# Write the real-time processed data to an output sink
query = clean_df\
    .writeStream \
    .format("kafka")\
    .outputMode("append") \
    .option("kafka.bootstrap.servers", f'{config["kafka"]["host"]}:{config["kafka"]["port"]}') \
    .option("topic", config['kafka']['topic2']) \
    .option("checkpointLocation", "checkpoints") \
    .start()\
    .awaitTermination()
    
    
