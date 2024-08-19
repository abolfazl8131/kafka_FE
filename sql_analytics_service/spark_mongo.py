from pyspark.sql import SparkSession
from config import config
from sql_queries import Q2

spark = SparkSession \
    .builder \
    .appName("spark-mongo") \
    .master('local')\
    .config("spark.mongodb.input.uri", config['mongo']['sparkuri']) \
    .config("spark.mongodb.output.uri", config['mongo']['sparkuri']) \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
    .getOrCreate()


tbl = spark.read\
    .format('com.mongodb.spark.sql.DefaultSource')\
    .option( "uri", config['mongo']['sparkuri']) \
    .load()

tbl.createOrReplaceTempView("tbl")

query1 = spark.sql(Q2)

query1.show()

