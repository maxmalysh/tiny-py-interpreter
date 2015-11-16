# Just a temporary solution for testing
for i in `seq 1 19`;
do
    path=tests/$i.txt
    echo $path
    python3 main.py $path
done

# Just a temporary solution for testing
for i in `seq 1 9`;
do
    path=tests/fail/$i.txt
    echo $path
    python3 main.py $path
done