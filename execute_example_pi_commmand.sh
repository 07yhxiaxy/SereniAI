#!/bin/bash
arg1="$1"
arg2="$2"
ssh pi@172.20.10.3 python "~/Desktop/CalHack/actuate.py $arg1 $arg2"
