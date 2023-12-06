
TESTING = True

# concept stuff...
source_start = 98
destination_start = 50
map_delta = destination_start - source_start
map_range = 2

for source in range(0, 100):
    if source >= source_start and source < source_start + map_range:
        print(f"{source=} = {(source+map_delta)=}")

if TESTING:
    file_name = 'test_input5'
else:
    file_name = 'my_input5'

# read file and get data
with open(file_name, 'r') as f:
    while x:=f.readline():
        line = x.rstrip()
        if "seeds: " in line:
            seeds = line.split("seeds: ")[1].split(" ")
