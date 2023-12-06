file_name = "input/adv1"
results = []
with open(file_name, "r") as f:
    while (x:= f.readline()):
        digits = {'first': None, 'last': None}
        for i in x:
            try:
                val = int(i)
                digits['last'] = val
                if digits['first'] == None:
                    digits['first'] = val
            except:
                None # not a digit
        results.append(digits)
    print(results)

total = 0
for i in results:
    total += i['first'] * 10 + i['last']
print(total)
