#!/bin/bash

#if [ -z "$1" ]; then
#	echo "Please provide lambda function name"
#    echo "e.g sh build.sh testfunction"
#    exit 1
#fi

#echo "Building Lambda Source File for function $1"
# sudo apt-get update -y
# sudo apt-get install -y python3-pip
# pip3 install -r requirements.txt -t src/package/

mkdir -p src/package
pip3 install -r requirements.txt -t src/package/

#cd src && zip -FSr ../${var.filename}.zip *
#rm -rf package
