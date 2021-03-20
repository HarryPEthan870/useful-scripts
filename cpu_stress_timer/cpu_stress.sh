#!/bin/bash
#Run yes on all cores
for i in $(seq $(getconf _NPROCESSORS_ONLN)); do yes > /dev/null & done
#take user input
echo "How long should this run for(in mins): "
read mintime
#convert to seconds
time=$(($mintime * 60))
#run python script
touch temps.txt
python3 timer.py $time