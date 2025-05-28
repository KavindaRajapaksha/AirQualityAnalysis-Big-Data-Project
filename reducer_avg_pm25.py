import sys

current_station = None
total = 0.0
count = 0.0

for line in sys.stdin:
    station, val = line.strip().split('\t')
    try:
        val = float(val)
    except:
        continue

    if station == current_station:
        total_val += val
        count += 1
    else:
        if current_station:
            print(f"{current_station}\t{total/count:.2f}")

        current_station = station
        total = val
        count = 1

if current_station:
    print(f"{current_station}\t{total/count:.2f}")
