card_extender = []
card_multiplier = []
total_score = 0
with open("my_input4", "r") as f:
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
                tmp_score += 1
        card_extender.append(tmp_score)
        card_multiplier.append(1)
        print(tmp_score)

print(f"{card_extender=}")


for i, ce in enumerate(card_extender):
    print(f"{card_multiplier=}")
    multiplier_start = i + 1
    multiplier_end = i + 1 + ce
    if multiplier_start >= len(card_multiplier):
        print(f"last card: {i=}, {ce=}")
        break
    if multiplier_end >= len(card_multiplier):
        multiplier_end = len(card_multiplier)
    for multiplier in range(card_multiplier[i]):
        for mi in range(multiplier_start, multiplier_end):
            card_multiplier[mi] += 1
print(card_multiplier)
print(sum(card_multiplier))