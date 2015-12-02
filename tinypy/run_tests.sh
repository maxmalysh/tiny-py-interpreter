#!/usr/bin/env bash
# Just a temporary solution for testing
for i in `seq 1 23`;
do
    path=tests/$i.txt
    echo $path
    python3 tinypy.py $path --parse
done

# Just a temporary solution for testing
for i in `seq 1 9`;
do
    path=tests/fail/$i.txt
    echo $path
    python3 tinypy.py $path --parse
done