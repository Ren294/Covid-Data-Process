#!/bin/bash

docker exec -it namenode bash -c "hdfs dfs -mkdir /data/ && \
hdfs dfs -chmod 777 /data && \
hdfs dfs -mkdir /data/covid_data && \
hdfs dfs -chmod 777 /data/covid_data && \
hdfs dfs -mkdir /data/kafka_data && \
hdfs dfs -chmod 777 /data/kafka_data"

docker exec -it kafka bash -c "
kafka-topics.sh --bootstrap-server localhost:9094 --create --topic covidin && \
kafka-topics.sh --bootstrap-server localhost:9094 --create --topic covidout"

docker exec -it spark-master bash -c "spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.apache.kafka:kafka-clients:3.2.0 /opt/spark-apps/streaming.py"