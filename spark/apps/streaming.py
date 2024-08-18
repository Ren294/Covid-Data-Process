from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
    .getOrCreate()

df = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "kafka:9094")\
    .option("subscribe", "covidin")\
    .option("startingOffsets", "earliest")\
    .option("failOnDataLoss", "false")\
    .load()

df = df.selectExpr("CAST(value AS STRING)")

df_1 = df.select(
    split(col("value"), ",").getItem(0).alias("iso"),
    split(col("value"), ",").getItem(1).alias("country"),
    split(col("value"), ",").getItem(2).alias("province"),
    split(col("value"), ",").getItem(5).cast(IntegerType()).alias("deaths"),
    split(col("value"), ",").getItem(9).cast(
        DoubleType()).alias("fatalityrate"),
    to_date(split(col("value"), ",").getItem(10), "yyyy-MM-dd").alias("date")
)

df_json = df_1.select(to_json(struct(*df_1.columns)).alias("value"))


def write_to_kafka(batch_df, batch_id):
    batch_df \
        .selectExpr("CAST(value AS STRING)") \
        .write \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9094") \
        .option("topic", "covidout") \
        .save()


query = df_json.writeStream \
    .foreachBatch(write_to_kafka) \
    .option("checkpointLocation", "file:///opt/spark-data/checkpoint") \
    .start()

query.awaitTermination()
