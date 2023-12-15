#!/usr/bin/env python3

#file_name = "input/adv10"
file_name = "input/test_adv10"

pipe_map = []
tile_map = {'|': {'N': True, 'E': False, 'S': True, 'W': False},
            '-': {'N': False, 'E': True, 'S': False, 'W': True},
            'L': {'N': True, 'E': True, 'S': False, 'W': False},
            'J': {'N': True, 'E': False, 'S': False, 'W': True},
            '7': {'N': False, 'E': False, 'S': True, 'W': True},
            'F': {'N': False, 'E': True, 'S': True, 'W': False},
            '.': {'N': False, 'E': False, 'S': False, 'W': False},
            'S': {'N': True, 'E': True, 'S': True, 'W': True}}
direction_from = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
dir_cycle = 'NESW'

def get_direction(dir):
    pos = dir_cycle.find(dir)
    try:
        new_dir = dir_cycle[pos + 1]
    except:
        new_dir = dir_cycle[0]
    return new_dir

def move_pos(direction, x, y):
    if direction == 'N':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'S':
        y += 1
    elif direction == 'W':
        x -= 1
    else:
        raise Exception(f"ERROR: invalid direction '{direction}' passed to function move_pos")
    return {'x': x, 'y': y}

def get_tile(x, y):
    return pipe_map[y][x]

def get_start():
    for y, row in enumerate(pipe_map):
        for x, tile in enumerate(row):
            if tile == 'S':
                return {'x': x, 'y': y}
    raise Exception(f"ERROR: start position not found")

with open(file_name, 'r') as f:
    while x:= f.readline().strip():
        pipe_map.append(x)

start_pos = get_start()
print(f"Start at {start_pos}")
current_position = start_pos
new_position = start_pos
steps = 0
current_direction = 'N'
for i in range(100):
    current_direction = get_direction(current_direction)
    new_position = move_pos(current_direction, **current_position)
    new_tile = get_tile(**new_position)
    if tile_map[new_tile][direction_from[current_direction]]:
        current_position = new_position
        current_direction = direction_from[current_direction]
        print(get_tile(**current_position))
        steps += 1
    else:
        None
        #print("no path")

    if current_position == start_pos:
        print(f"completed circle in {steps} steps")
        break

print(f"farthest position: {steps /2 }")