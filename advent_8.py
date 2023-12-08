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
