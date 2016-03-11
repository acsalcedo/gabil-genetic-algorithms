#!/bin/bash

for i in `seq 1 10`;
do
    echo "Run " $i
    python main.py -p positive.data -n negative.data -c 0.8 -m 0.01 -s 2 -e 1 -i 60 -x 1
done
