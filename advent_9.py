#!/usr/bin/env python3

file_name = "input/adv9"
#file_name = "input/test_adv9"

all_inputs = []
with open(file_name, 'r') as f:
    while x:= f.readline().rstrip():
        all_inputs.append(list(map(int, x.split(' '))))
#print(all_inputs)

all_numbers_added = 0
for input in all_inputs:
    tmp_lists = [input]
    added_numbers = 0
    for number_list in tmp_lists:
        tmp_list = []
        for i in range(len(number_list) - 1):
            tmp_list.append(number_list[i + 1] - number_list[i])
        else:
            try:
                for el in tmp_list:
                    if el != 0:
                        break
                else:
                    print(f" all zeroes: {tmp_list}")
                    added_numbers += number_list[-1:][-1]
                    break
            except:
                print("ERROR: break because empty!")
                break
            tmp_lists.append(tmp_list)
        #print(tmp_list[-1:][-1])
        added_numbers += number_list[-1:][-1]
        #print(f"...added: {number_list[-1:][-1]}")

    print(added_numbers)
    all_numbers_added += added_numbers

print(all_numbers_added)