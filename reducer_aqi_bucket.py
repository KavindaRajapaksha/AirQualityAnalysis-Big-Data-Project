#!/usr/bin/env python3
import sys
from collections import defaultdict

current_date = None
bucket_counts = defaultdict(int)

for line in sys.stdin:
    try:
        date, bucket = line.strip().split('\t')
        if date == current_date:
            bucket_counts[bucket] += 1
        else:
            if current_date:
                for b, count in bucket_counts.items():
                    print(f"{current_date}\t{b}\t{count}")
            current_date = date
            bucket_counts = defaultdict(int)
            bucket_counts[bucket] = 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if current_date:
    for b, count in bucket_counts.items():
        print(f"{current_date}\t{b}\t{count}")