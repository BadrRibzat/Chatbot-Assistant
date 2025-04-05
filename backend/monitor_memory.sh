#!/bin/bash
PID=$1
while [ -d /proc/$PID ]; do
    cat /proc/$PID/status | grep VmRSS
    sleep 0.5
done
