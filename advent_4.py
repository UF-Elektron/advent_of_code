
total_score = 0
with open("test_input4", "r") as f:
    while (x:=f.readline()):
        _card, data = x.strip().split(':')
        win, my_val = data.split('|')
        win_list = win.split(' ')
        my_val_list = my_val.split(' ')

        win_list_int = [int(i) for i in win_list if i != '']
        my_list_int = [int(i) for i in my_val_list if i != '']

        tmp_score = 0
        for my_val in my_list_int:
            if my_val in win_list_int:
                if tmp_score == 0:
                    tmp_score = 1
                else:
                    tmp_score *= 2
        print(f"card score:  {tmp_score}")
        total_score += tmp_score
print(total_score)