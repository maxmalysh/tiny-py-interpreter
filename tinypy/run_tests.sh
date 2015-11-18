#!/usr/bin/env bash
# Just a temporary solution for testing
for i in `seq 1 20`;
do
    path=tests/$i.txt
    echo $path
    python3 tinypy.py $path
done

# Just a temporary solution for testing
for i in `seq 1 9`;
do
    path=tests/fail/$i.txt
    echo $path
    python3 tinypy.py $path
done