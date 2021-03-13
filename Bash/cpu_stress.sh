#!/bin/bash
#Run yes on all cores
for i in $(seq $(getconf _NPROCESSORS_ONLN)); do yes > /dev/null & done
#take user input
echo "How long do you want run the stress test for(in minutes)?"
read mintime
#convert to seconds 
time=$(($mintime * 60))
#set desingated time
sleep $time && killall yes 
