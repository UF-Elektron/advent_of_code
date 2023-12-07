#!/usr/bin/env python3
TESTING = False

if TESTING:
    file_name = 'input/test_adv5'
else:
    file_name = 'input/adv5'

maps = {}
map_names = []

# read file and get data
with open(file_name, 'r') as f:
    map_name = ''
    while x:=f.readline():
        line = x.rstrip()
        if "seeds: " in line:
            seeds_data = line.split("seeds: ")[1].split(" ")
            seeds_data = [int(s) for s in seeds_data]
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

# wow... my solution from part 1 does not scale at all!
min_value = None
all_results = []
# part 2 with seed ranges
seeds_length = len(seeds_data)
print(f"{seeds_length=}")
seeds_generator = []
for i in range(0, seeds_length, 2):
    print(f"create iterator {i}")
    seeds_generator = (seeds_data[0 + i] + s for s in range(seeds_data[1 + i]))
    #seeds_generator.append(x)
    #break

    #print(seeds)
    # map values
    #for seeds in seeds_generator:
    for seed in seeds_generator:
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
        if min_value:
            if min_value > mapped_value:
                min_value = mapped_value
        else:
            min_value = mapped_value
        # all_results.append(mapped_value)
        #print(f"{seed}: {mapped_value}")
    # part 1
    #print(min(all_results))
    # part 2
    print(min_value)
    # 46 +