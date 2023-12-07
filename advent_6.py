file_name = "input/adv6"
#file_name = "input/test_adv6"

time = 0
distance = 0
with open(file_name, 'r') as f:
    while x:= f.readline().rstrip():
        if "Time:" in x:
            time = x.split("Time:")[1].split(" ")
        elif "Distance:" in x:
            distance = x.split("Distance:")[1].split(" ")
        else:
            print("ooops")

time = [int(t) for t in time if t != '']
distance = [int(d) for d in distance if d != '']

multiplied = 1
for i in range(len(time)):
    solution = 0
    for t in range(time[i] + 1):
        res = (time[i] - t) * (t * 1)
        if res > distance[i]:
            solution += 1
    multiplied *= solution
print(multiplied)