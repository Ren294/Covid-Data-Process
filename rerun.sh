if [ -f hiveconf/hiveserver2.pid ]; then
    rm hiveconf/hiveserver2.pid
fi

if [ -d spark/data/checkpoint ]; then
    rm -r spark/data/checkpoint
fi
