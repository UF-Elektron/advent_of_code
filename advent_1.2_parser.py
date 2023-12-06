file_name = "input/adv1"
valid_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_lookup = {'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9}

results = []
with open(file_name, "r") as f:
    while (x:= f.readline()):
        digits = {'first': None, 'last': None}
        for i, el in enumerate(x):
            try:
                val = int(el)
                digits['last'] = val
                if digits['first'] == None:
                    digits['first'] = val
            except:
                for valid_digit in valid_digits:
                        found = False
                        for offset, character in enumerate(valid_digit):
                            if len(x) <= i + offset:
                                # break because out of range
                                break
                            if x[i + offset] == character:
                                #print("yee")
                                found = True
                            else:
                                #found = False
                                break
                                #print("not this one")
                        else:
                            if found == True:
                                print(f"found :-) ---> {valid_digit}")
                                if digits['first'] == None:
                                    digits['first'] = digit_lookup[valid_digit]
                                digits['last'] = digit_lookup[valid_digit]
                            else:
                                None
                                #print("not found!?!?!?")

        results.append(digits)
    print(results)

total = 0
for i in results:
    total += i['first'] * 10 + i['last']
print(total)
