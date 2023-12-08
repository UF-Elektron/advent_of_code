#file_name = "input/adv7"
file_name = "input/test_adv7"

hands = []
with open(file_name, 'r') as f:
    while(x:= f.readline().rstrip()):
        print(x)
        cards, bid = x.split(" ")
        hands.append({'cards': cards, 'bid': bid, 'type': 0})
print(hands)

# map card points
map_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
all_cards = "AKQJT98765432"

# fand hand types
for hand in hands:
    countings = []
    for a_card in all_cards:
        print(f"{a_card}: {hand['cards'].count(a_card)}")
        countings.append(hand['cards'].count(a_card))
    print(countings)
    max_type = max(countings)
    print(f"{max_type=}")

    if max_type > 3:
        hand['type'] = max_type
    elif max_type == 3:
        countings.remove(3)
        if max(countings) == 2:
            hand['type'] = 3
        else:
            hand['type'] = 2
    elif max_type == 2:
        countings.remove(2)
        if max(countings) == 2:
            hand['type'] = 1
        else:
            hand['type'] = 0
    else:
        hand['type'] = -1

print(hands)
#hand_types = [-1, 0, 1, 2, 3, 4, 5]
#for hand_type in hand_types:

#max_hand_type = -1
## bubble sort order
#for hand in hands:
#    if hand['type'] > max_hand_type:
#        hand_ordered['type'] = hand['type']
#        hand_ordered['bid'] = hand['bid']

# too tired to figure out bubble sort... do this tomorrow
#hands_tmp = {'cards': '12345', 'bid': 69, 'type': -1}
for i in range(len(hands)):
    try:
        # determine higher type and order accordingly
        if hands[i]['type'] > hands[i + 1]['type']:
            hands_tmp = hands[i]
            hands[i] = hands[i + 1]
            hands[i + 1]  = hands_tmp
        # when type equal determine higher start card
        elif hands[i]['type'] == hands[i + 1]['type']:
            cards0 = hands[i]['cards']
            cards1 = hands[i + 1]['cards']
            for j in len(cards0):
                if cards0[j] > cards1[j]:
                    print("cards0 wins")
                elif cards0[j] < cards1[j]:
                    print("cards1 wins")
                else:
                    print("draw")
    except:
        print("last element")
print(hands)