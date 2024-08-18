#!/bin/bash

docker exec -it notebook jupyter server list | awk -F'token=' '{print $2}' | awk -F'/' '{print $1}' | sed 's/ ::.*//'