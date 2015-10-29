# Just a temporary solution for testing
for i in `seq 0 16`;
do
    echo tests/$i.txt
    python3 main.py tests/$i.txt
done