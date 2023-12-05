digits = '0123456789'
not_a_symbol = digits + '.'
checked_element_offsets = [-1, 0, 1]

part_numbers = []
invalid_numbers = []
data_buffer = []

with open("test_input3", "r") as f:
    while (x:= f.readline()):
        data_buffer.append(x)

for i in data_buffer:
    print(i)

line_before = data_buffer[0]
line_current = data_buffer[1]
line_after = data_buffer[2]

def symbol_nearby(pos):
    for line in [line_before, line_after, line_current]:
        for check_el_offset in checked_element_offsets:
            try:
                if line[pos + check_el_offset] not in not_a_symbol:
                    print(f"symbol found: {line[pos + check_el_offset]}")
                    return True
            except:
                print("out of matrix")
    return False

for i, x in enumerate(data_buffer):
    tmp_nr = ''
    valid = False
    for pos, el in enumerate(x): # + '.'?
        if el in digits:
            # it's a number
            tmp_nr += el
            if symbol_nearby(pos):
                valid = True
        else:
            if valid:
                part_numbers.append(tmp_nr)
            else:
                invalid_numbers.append(tmp_nr)
            tmp_nr = ''
            valid = False
    line_before = data_buffer[i]
    try:
        line_current = data_buffer[i + 1]
    except:
        print("end of data buffer")
        line_after = ['.']
    try:
        line_after = data_buffer[i + 2]
    except:
        print("end of data buffer")
        line_after = ['.']


total = 0
for part_nr in part_numbers:
    total += int(part_nr)
print(part_numbers)
print(invalid_numbers)
print(f"part number total: " + str(total))