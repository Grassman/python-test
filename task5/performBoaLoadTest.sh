#!/bin/sh
if [ "$#" -ne 2 ]; then
  echo "Usage: ./performBoaLoadTest.sh <number of requests per usa case> <number of concurrent threads per use case>" >&2
  exit 1
fi
echo Doing $1 requests for http://ubuntu/ with the concurrency of $2. Result can be read in listingResult.txt &
ab -n $1 -c $2 http://ubuntu/ > listingResult.txt &
echo Doing $1 requests for http://ubuntu/dev/test.py with the concurrency of $2. Result can be read in smallFileResult.txt &
ab -n $1 -c $2 http://ubuntu/dev/test.py > smallFileResult.txt &
echo Doing $1 requests for http://ubuntu/dev/python-test/dbus-python-1.1.1.tar with the concurrency of $2. Result can be read in biggerFileResult.txt &
ab -n $1 -c $2 http://ubuntu/dev/python-test/dbus-python-1.1.1.tar > biggerFileResult.txt &
echo All tests started. See log files for result!

