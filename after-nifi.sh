#!/bin/bash

docker exec -it namenode bash -c "hdfs dfs -chmod -R 777 /data/"

docker exec -it spark-master bash -c "service ssh start"

docker exec -it spark-master bash -c "spark-sql -f /opt/spark-apps/createDB.sql"