digits = '0123456789'
not_a_symbol = digits + '.'
a_gear = '*'
checked_element_offsets = [-1, 0, 1]

part_numbers = []
invalid_numbers = []
data_buffer = []

with open("my_input3", "r") as f:
    while (x:= f.readline()):
        data_buffer.append(x.rstrip() + '..')

line_before = '.'
line_current = data_buffer[0]
line_after = data_buffer[1]

def symbol_nearby(pos):
    for line in [line_before, line_after, line_current]:
        for check_el_offset in checked_element_offsets:
            try:
                if line[pos + check_el_offset] not in not_a_symbol:
                    print(f"symbol found: {line[pos + check_el_offset]}\n in {line=}\n at {pos=}")
                    return True
            except:
                None
    return False

gears_with_numbers = {}
def gear_nearby(pos, line_nr):
    res = []
    for line_offset in checked_element_offsets:
        line_nr_tmp = line_nr + line_offset
        try:
            line = data_buffer[line_nr_tmp]
        except:
            line = '.'
        for check_el_offset in checked_element_offsets:
            try:
                gear_pos = pos + check_el_offset
                if line[pos + check_el_offset] in a_gear:
                    print(f"gear '*' found: {line_nr_tmp=} {gear_pos=}")
                    res.append((line_nr_tmp, gear_pos))
            except:
                None
    return res

for i, x in enumerate(data_buffer):
    tmp_nr = ''
    valid = False
    line_coord = []
    for pos, el in enumerate(x):
        if el in digits:
            # it's a number
            tmp_nr += el
            if symbol_nearby(pos):
                valid = True
            if line_coord == []:
                line_coord = gear_nearby(pos, i)
                print(f"received {line_coord=}")
        else:
            if tmp_nr != '':
                if valid:
                    part_numbers.append(tmp_nr)
                else:
                    invalid_numbers.append(tmp_nr)
                for lc in line_coord:
                    try:
                        gears_with_numbers.get(lc[0]).get(lc[1]).append(tmp_nr)
                        print(f"updated entry for {lc=}")
                    except:
                        try:
                            print(f"updated ***************** entry for {lc=}")
                            gears_with_numbers.get(lc[0]).update({lc[1]: [tmp_nr]})
                        except:
                            print(f"create new entry for {lc=}")
                            gears_with_numbers.update({lc[0]: {lc[1]: [tmp_nr]}})
            line_coord = []
            tmp_nr = ''
            valid = False

total = 0
for part_nr in part_numbers:
    total += int(part_nr)
print(part_numbers)
print(f"part number total: " + str(total))

print(gears_with_numbers)
summed_up = 0
for k in gears_with_numbers.keys():
    for k2 in gears_with_numbers[k].keys():
        if len(gears_with_numbers[k][k2]) == 2:
            print(gears_with_numbers[k][k2])
            summed_up += int(gears_with_numbers[k][k2][0]) * int(gears_with_numbers[k][k2][1])
        else:
            print(f"invalid length: {gears_with_numbers[k][k2]}")
print(summed_up)