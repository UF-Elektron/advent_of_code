file_name = "input/adv8"
#file_name = "input/test_adv8"

directions = None
# the first key is the location and the sub keys are left and right destination
# e.g.: {'11A': {'L': '11B', 'R': 'XXX'}}
coordinates = {}

with open(file_name, 'r') as f:
    while(x:=f.readline()):
        x = x.strip()
        if " = " not in x and directions is None:
            directions = x
        elif x != '':
            location, destination_set = x.split("=")
            striiiiiiped = destination_set.strip(" ()")
            l, r = striiiiiiped.split(',')
            l = l.strip()
            r = r.strip()
            coordinates.update({location.strip(): {'L': l, 'R':r}})

# find start location: last element is 'A'
start_indicator = 'A'
start_locations = []
for i in coordinates.keys():
    if i[2] == start_indicator:
        start_locations.append(i)

# find destination: last element is 'Z'
destination_indicator = 'Z'
destination_locations = []
for i in coordinates.keys():
    if i[2] == destination_indicator:
        destination_locations.append(i)

# particular destination reached: number of reaches + steps (append to list)
all_paths = []
# [{target1: {reached_count = 0, steps: []}, {target2: {reached_count = 0, steps: []}, current_location: {location_id: {'L': '11B', 'R': 'XXX'}}}, ...]
for start_lociation in start_locations:
    all_paths.append({'current_location': {start_lociation: coordinates[start_lociation]}})

# prepare dictionaries in all_paths with necessary counters
for path in all_paths:
    for destination_location in destination_locations:
        path.update({destination_location: {'reached_count': 0, 'steps': []}})

# find out how many steps are needed to reach the locations
# ugly solution:
# - better not loop in range but loop as long as steps to destination are not known (and repeated steps for that matter)
# - dictionary structure a bit unwieldy... have to get key name buy doing ugly botch with list(x.keys())[0]... this means dict structure is not correct!
direction_iterator = 0
for i in range(100000):
    next_diretion = directions[direction_iterator]
    for path in all_paths:
        lid = list(path['current_location'].keys())[0]
        location_id = path['current_location'][lid][next_diretion]
        path.update({'current_location': {location_id: coordinates[location_id]}})
        for destination_location in destination_locations:
            lid = list(path['current_location'].keys())[0]
            x = path.get(destination_location)
            if lid == destination_location:
                x['reached_count'] += 1
                x['steps'].append(i + 1)

    if direction_iterator == len(directions) - 1:
        direction_iterator = 0
    else:
        direction_iterator += 1

steps_delta = []
for path in all_paths:
    for destination_location in destination_locations:
        x = path.get(destination_location)
        if x['reached_count'] > 0:
            steps_delta.append(x['steps'][0])
            continue
print(steps_delta)

# find least common multiple (Kleinstes gemeinsames Vielfaches)
# python math library is awesome :-)
import math
print(math.lcm(*steps_delta))


# results after completing search for steps "for i in range(100000):"
{'current_location': {'XRG': {'L': 'LNK', 'R': 'KQL'}}, 'LFZ': {'reached_count': 0, 'steps': []},
   'HMZ': {'reached_count': 4, 'steps': [20777, 41554, 62331, 83108]},}                               # 'ZZZ': {'reached_count': 0, 'steps': []}, 'DDZ': {'reached_count': 0, 'steps': []}, 'XKZ': {'reached_count': 0, 'steps': []}, 'RNZ': {'reached_count': 0, 'steps': []}}
{'current_location': {'LHL': {'L': 'HSC', 'R': 'LBV'}}, 'LFZ': {'reached_count': 0, 'steps': []}, 'HMZ': {'reached_count': 0, 'steps': []},
   'ZZZ': {'reached_count': 5, 'steps': [18673, 37346, 56019, 74692, 93365]},}                        # 'DDZ': {'reached_count': 0, 'steps': []}, 'XKZ': {'reached_count': 0, 'steps': []}, 'RNZ': {'reached_count': 0, 'steps': []}}
{'current_location': {'MBH': {'L': 'KBF', 'R': 'TSX'}}, 'LFZ': {'reached_count': 0, 'steps': []}, 'HMZ': {'reached_count': 0, 'steps': []}, 'ZZZ': {'reached_count': 0, 'steps': []}, 'DDZ': {'reached_count': 0, 'steps': []}, 'XKZ': {'reached_count': 0, 'steps': []},
   'RNZ': {'reached_count': 7, 'steps': [13939, 27878, 41817, 55756, 69695, 83634, 97573]}}
{'current_location': {'JNK': {'L': 'RXN', 'R': 'BQX'}}, 'LFZ': {'reached_count': 0, 'steps': []}, 'HMZ': {'reached_count': 0, 'steps': []}, 'ZZZ': {'reached_count': 0, 'steps': []}, 'DDZ': {'reached_count': 0, 'steps': []},
   'XKZ': {'reached_count': 5, 'steps': [17621, 35242, 52863, 70484, 88105]},}                        # 'RNZ': {'reached_count': 0, 'steps': []}}
{'current_location': {'QNX': {'L': 'SHD', 'R': 'LXG'}},
   'LFZ': {'reached_count': 5, 'steps': [19199, 38398, 57597, 76796, 95995]},}                        # 'HMZ': {'reached_count': 0, 'steps': []}, 'ZZZ': {'reached_count': 0, 'steps': []}, 'DDZ': {'reached_count': 0, 'steps': []}, 'XKZ': {'reached_count': 0, 'steps': []}, 'RNZ': {'reached_count': 0, 'steps': []}}
{'current_location': {'NQL': {'L': 'MGL', 'R': 'SCP'}}, 'LFZ': {'reached_count': 0, 'steps': []}, 'HMZ': {'reached_count': 0, 'steps': []}, 'ZZZ': {'reached_count': 0, 'steps': []},
   'DDZ': {'reached_count': 8, 'steps': [12361, 24722, 37083, 49444, 61805, 74166, 86527, 98888]},}   #'XKZ': {'reached_count': 0, 'steps': []}, 'RNZ': {'reached_count': 0, 'steps': []}}