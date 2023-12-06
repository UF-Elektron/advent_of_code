#!/usr/bin/env python3
TESTING = True

# concept stuff...
source_start = 0
destination_start = 0
map_delta = destination_start - source_start
map_range = 0

# for source in range(0, 100):
#     if source >= source_start and source < source_start + map_range:
        # print(f"{source=} = {(source+map_delta)=}")

if TESTING:
    file_name = 'test_input5'
else:
    file_name = 'my_input5'

maps = {}

# read file and get data
with open(file_name, 'r') as f:
    map_name = ''
    while x:=f.readline():
        line = x.rstrip()
        if "seeds: " in line:
            seeds = line.split("seeds: ")[1].split(" ")
        elif " map:" in line:
            map_name = line.split(" map:")[0]
            print(map_name)
        else:
            try:
                destination_start, source_start, map_range = line.split(' ')
                destination_start = int(destination_start)
                source_start = int(source_start)
                map_range = int(map_range)
            except:
                print(f"... empty line: '{line}'")
                continue

            if destination_start != '':
                map_info = {"source_start": source_start, "destination_start": destination_start, 'map_range': map_range}
                try:
                    maps[map_name].append(map_info)
                except:
                    maps.update({map_name: [map_info]})

for k in maps.keys():
    print(k)
    print(maps[k])
