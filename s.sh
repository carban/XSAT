#!/bin/sh

for file in instances/*
do
    filename=$(echo $file | sed 's/instances//g')
    python newxsat.py $file $1 > reduced/$filename
    echo "Done"
done