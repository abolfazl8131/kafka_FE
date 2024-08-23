from pyspark.sql import SparkSession
from config import config
from sql_queries import Q2,Q1
import matplotlib.pyplot as plt

spark = SparkSession \
    .builder \
    .appName("spark-mongo") \
    .master('local')\
    .config("spark.mongodb.input.uri", config['mongo']['uri']) \
    .config("spark.mongodb.output.uri", config['mongo']['uri']) \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
    .getOrCreate()


tbl = spark.read\
    .format('com.mongodb.spark.sql.DefaultSource')\
    .option( "uri", config['mongo']['uri']) \
    .load()

tbl.createOrReplaceTempView("tbl")

query1 = spark.sql(Q1)

df = query1.toPandas()

plt.scatter(df['latitude'], df['longitude'])
plt.xlabel("lat")
plt.ylabel("long")
plt.title("latlong")
plt.savefig('plt.png')
