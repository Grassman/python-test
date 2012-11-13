#!/bin/bash
id=0; tot=0; p_id=0; p_tot=0;
sleep=30;
echo "Starting to probe at `date`" >> probe.log;
while true; do
    p_id=$id; p_tot=$tot;
    x=`cat /proc/stat | grep -w cpu`;
    id=`echo $x | cut -d " " -f 5`;
    tot=0;
    for f in `echo $x`; do
        tot=$(($tot + $f));
    done; 
    echo "Cpu and mem at `date`: " >> probe.log;
    echo "Cpu usage% = "$((100 -(($id - $p_id)*100/($tot - $p_tot)))) >> probe.log;
    free -m >> probe.log;
    echo "Open files/sockets by www-data `lsof -u www-data | wc -l`" >> probe.log;
    echo "---" >> probe.log;
    sleep $sleep;
done
