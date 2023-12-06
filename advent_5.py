#!/usr/bin/env python3
TESTING = False

if TESTING:
    file_name = 'test_input5'
else:
    file_name = 'my_input5'

maps = {}
map_names = []

# read file and get data
with open(file_name, 'r') as f:
    map_name = ''
    while x:=f.readline():
        line = x.rstrip()
        if "seeds: " in line:
            seeds = line.split("seeds: ")[1].split(" ")
            seeds = [int(s) for s in seeds]
        elif " map:" in line:
            map_name = line.split(" map:")[0]
            map_names.append(map_name)
            #print(map_name)
        else:
            try:
                destination_start, source_start, map_range = line.split(' ')
                destination_start = int(destination_start)
                source_start = int(source_start)
                map_range = int(map_range)
            except:
                # empty line
                #print(f"... empty line: '{line}'")
                continue

            if destination_start != '':
                map_info = {'source_start': source_start, 'destination_start': destination_start, 'map_range': map_range}
                try:
                    maps[map_name].append(map_info)
                except:
                    maps.update({map_name: [map_info]})

# map values
all_results = []
for seed in seeds:
    mapped_value = seed
    for name in map_names:
        for m in maps[name]:
            source_start = m['source_start']
            destination_start = m['destination_start']
            map_range = m['map_range']
            map_delta = destination_start - source_start
            #print(f"{source_start} <= my_val < {source_start + map_range}")
            if mapped_value >= source_start and mapped_value < source_start + map_range:
                mapped_value = mapped_value + map_delta
                break
    all_results.append(mapped_value)
    print(f"{seed}: {mapped_value}")

print(min(all_results))