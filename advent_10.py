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
dir_map = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
dir_cycle = ['NESW']

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
    return (x, y)

def get_direction_from(direction_to):
    return dir_map(direction_to)

def get_start():
    for y, row in enumerate(pipe_map):
        for x, tile in enumerate(row):
            if tile == 'S':
                return (x, y)
    raise Exception(f"ERROR: start position not found")

with open(file_name, 'r') as f:
    while x:= f.readline().strip():
        pipe_map.append(x)


x, y = get_start()
print(f"Start at {x}x {y}y")
start_pos = {'x': x, 'y': y}
print(start_pos)
#print(move_pos('S', x, y))
