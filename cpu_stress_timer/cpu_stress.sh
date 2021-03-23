#!/bin/bash
#Run yes on all cores
for i in $(seq $(getconf _NPROCESSORS_ONLN)); do yes > /dev/null & done
#take user input
mintime=$1
#convert to seconds
time=$(($mintime * 60))
#run python script
touch temps.txt
sleep 3
python3 timer.py $time