#file_name = "input/adv8"
file_name = "input/test_adv8"

directions = None
coordinates = {}
with open(file_name, 'r') as f:
    while(x:=f.readline()):
        x = x.strip()
        if " = " not in x and directions is None:
            directions = x
        elif x != '':
            print(x)

            location, destination_set = x.split("=")
            striiiiiiped = destination_set.strip(" ()")
            l, r = striiiiiiped.split(',')
            l = l.strip()
            r = r.strip()
            coordinates.update({location.strip(): {'L': l, 'R':r}})

print(directions)
print(coordinates)

# find 'ZZZ'
location = 'AAA'
iterations = 0
total_steps = 0
while location != 'ZZZ':
    total_steps += 1
    next_diretion = directions[iterations]
    location = coordinates[location][next_diretion]
    print(f"new location = {location}")
    if iterations == len(directions) - 1:
        iterations = 0
    else:
        iterations += 1
print(f"total steps required to reach destination: {total_steps}")