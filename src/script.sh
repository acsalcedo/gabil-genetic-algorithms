#!/bin/bash

for i in `seq 1 10`;
do
    echo "Run " $i
    python main.py -f crx.data -c 0.6 -m 0.01 -g 1000
done
