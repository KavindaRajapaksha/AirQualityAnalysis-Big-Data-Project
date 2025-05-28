import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  

for row in reader:
    try:
        datetime = row[1]
        aqi_bucket = row[3]
        if aqi_bucket and aqi_bucket != 'NA':
            date = datetime.split(' ')[0]
            print(f"{date}\t{aqi_bucket}")
    except:
        continue
