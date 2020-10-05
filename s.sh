#!/bin/sh

for file in instancias/*
do
    filename=$(echo $file | sed 's/instancias//g')
    (python newxsat.py < $file) > reduced/$filename
    echo "Done"
done