#!/bin/bash
ENV_FILE=".env"

NEW_UID=$(id -u)

if [ -f "$ENV_FILE" ]; then
  sed -i '/^AIRFLOW_UID=/d' "$ENV_FILE"
  
  echo "AIRFLOW_UID=$NEW_UID" >> "$ENV_FILE"
else
  echo "AIRFLOW_UID=$NEW_UID" > "$ENV_FILE"
fi
mkdir -p spark/apps spark/data

mkdir -p \
nifi/content_repository \
nifi/database_repository \
nifi/flowfile_repository \
nifi/logs \
nifi/provenance_repository \
nifi/state
touch nifi/env.properties
echo “nifi.security.user.login.identity.provider=single-user-provider” > nifi/env.properties


if [ -f hiveconf/hiveserver2.pid ]; then
    rm hiveconf/hiveserver2.pid
fi

if [ -d spark/data/checkpoint ]; then
    rm -r spark/data/checkpoint
fi

docker-compose up airflow-init