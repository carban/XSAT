#!/bin/sh

for file in InstanciasSAT/*
do
    filename=$(echo $file | sed 's/InstanciasSAT//g')
    python Reductor/newxsat.py $file $1 > X-SAT/$filename
    echo $filename "Done"
done
