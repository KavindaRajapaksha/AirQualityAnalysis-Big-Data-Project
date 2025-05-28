#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # skip header

for row in reader:
    try:
        datetime = row[1]
        aqi_bucket = row[3]
        if aqi_bucket and aqi_bucket != 'NA':
            date = datetime.split(' ')[0]
            print(f"{date}\t{aqi_bucket}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)