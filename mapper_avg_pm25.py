#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  

for row in reader:
    try:
        station = row[0]
        pm25 = row[2]
        if pm25 != '' and pm25 != 'NA':
            print(f"{station} \t {pm25}")
    except:
        continue