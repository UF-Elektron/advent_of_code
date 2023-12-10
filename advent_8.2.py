#file_name = "input/adv8"
file_name = "input/test_adv8"

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

#print(directions)
#print(coordinates)

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

for path in all_paths:
    for destination_location in destination_locations:
        path.update({destination_location: {'reached_count': 0, 'steps': []}})
print(all_paths)

# find out how many steps are needed to reach the locations
direction_iterator = 0
for i in range(10):
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
print(all_paths)
#print(all_paths)