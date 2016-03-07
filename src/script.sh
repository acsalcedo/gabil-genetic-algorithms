#!/bin/bash

for i in `seq 1 10`;
do
    echo "Run " $i
    python main.py -f data -c 0.6 -m 0.001
done