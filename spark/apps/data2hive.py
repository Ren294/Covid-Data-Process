from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("COVID Data Processing") \
    .master("spark://spark-master:7077") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse")\
    .config("spark.sql.catalogImplementation", "hive")\
    .enableHiveSupport() \
    .getOrCreate()

schema = StructType([
    StructField("country_code", StringType(), True),
    StructField("country_name", StringType(), True),
    StructField("iso_code", StringType(), True),
    StructField("total_cases", IntegerType(), True),
    StructField("new_cases", IntegerType(), True),
    StructField("total_deaths", IntegerType(), True),
    StructField("new_deaths", IntegerType(), True),
    StructField("total_recovered", IntegerType(), True),
    StructField("new_recovered", IntegerType(), True),
    StructField("case_fatality_rate", DoubleType(), True),
    StructField("date_reported", DateType(), True)
])

df = spark.read.csv("hdfs://namenode:9000/data/covid_data",
                    schema=schema, header=False)

df.write.mode("overwrite").saveAsTable("covid_db.covid_data")
