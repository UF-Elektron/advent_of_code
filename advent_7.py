file_name = "input/adv7"
#file_name = "input/test_adv7"

# map card points
# part 1 map
#map_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
# part 2 map
map_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
all_cards = "AKQJT98765432"
card_types = [-1, 0, 1, 2, 3, 4, 5]

# create card points list (for determining winner when type is equal)
def card_points(cards):
    card_points = []
    for card in cards:
        tmp_point = map_card.get(card, None)
        if tmp_point is None:
            tmp_point = int(card)
        card_points.append(tmp_point)
    return card_points

hands = []
with open(file_name, 'r') as f:
    while(x:= f.readline().rstrip()):
        cards, bid = x.split(" ")
        card_point_list = card_points(cards)
        hands.append({'cards': cards, 'card_points': card_point_list, 'bid': bid, 'type': 0})

# hand types
for hand in hands:
    joker_count = hand['cards'].count('J')
    print(f"super special joker card(s) = {joker_count}")
    countings = [] # {'card': 'J', 'amount': 1}
    for a_card in all_cards:
        #print(f"{a_card}: {hand['cards'].count(a_card)}")
        countings.append({'card': a_card, 'amount': hand['cards'].count(a_card)})
    #print(countings)
    countings = sorted(countings, key=lambda count_el: count_el['amount'], reverse=True)
    max_type = countings[0]['amount']
    second_to_max_type = countings[1]['amount']
    print(f"{max_type=}")

    #print(f"{promoted_card_type=}")

    promoted_card_count = 0
    promoted_card_count_total = 0
    if joker_count > 0:
        promoted_card_type = countings[0]['card']
        promoted_card_count = countings[0]['amount']
        for cunt in countings:
            if cunt['amount'] >= max_type:
                if card_points([promoted_card_type]).pop() > card_points([cunt['card']]).pop():
                    if cunt['card'] != 'J':
                        promoted_card_type = cunt['card']
                        promoted_card_count = cunt['amount']
        if promoted_card_type == 'J':
            promoted_card_type = countings[1]['card']
            promoted_card_count = countings[1]['amount']

        promoted_card_count_total = promoted_card_count + joker_count
        print(f"{promoted_card_type=}")
        print(f"{promoted_card_count=}")
        print(f"{joker_count=}")
        print(f"**{promoted_card_count_total=}")
        max_type = promoted_card_count_total

    if max_type > 3:
        hand['type'] = max_type
    elif max_type == 3:
        if second_to_max_type == 2:
            hand['type'] = 3
        else:
            hand['type'] = 2
    elif max_type == 2:
        if second_to_max_type == 2:
            hand['type'] = 1
        else:
            hand['type'] = 0
    else:
        hand['type'] = -1

print(hands)

# sorted is a cool function :-)
hands_sorted_by_type = sorted(hands, key=lambda hand: hand['type'])
card_type_old = -1
equal_type_ranges = []
index_old = 0
# hands_sorted_by_type = [{'cards': '32T3K', 'card_points': [3, 2, 10, 3, 13], 'bid': '765', 'type': 1},
#                         {'cards': 'KK677', 'card_points': [13, 13, 6, 7, 7], 'bid': '28', 'type': 1},
#                         {'cards': 'KTJJT', 'card_points': [13, 10, 11, 11, 10], 'bid': '220', 'type': 4},
#                         {'cards': 'T55J5', 'card_points': [12, 5, 5, 11, 5], 'bid': '684', 'type': 4},
#                         {'cards': 'QQQJA', 'card_points': [11, 12, 12, 11, 14], 'bid': '483', 'type': 4}]

# if card types are equal do a sort for this range only
for index, handyhand in enumerate(hands_sorted_by_type): # + [{'cards': 'None', 'card_points': [0]*5, 'bid': 0, 'type': 0}]):
        # if card_type_old is None:
        #     card_type_old = handyhand['type']
        if card_type_old != handyhand['type']:# or index == len(hands_sorted_by_type) - 1:
            card_type_old = handyhand['type']
            #print(f"{index=}")
            if index - index_old > 1:# or index == len(hands_sorted_by_type) - 1:
                # sort
                #print(f"sort from {index_old} to {index - 1}")
                hands_sorted_by_type[index_old : index]= sorted(hands_sorted_by_type[index_old : index], key=lambda hand: hand['card_points'])
                #print(sorted(hands_sorted_by_type[index_old : index], key=lambda hand: hand['card_points']))
            index_old = index
            #equal_type_ranges.append(index)
else:
    if len(hands_sorted_by_type) - 1 != index_old:
        #print(f"sort from {index_old} to {len(hands_sorted_by_type) - 1}")
        hands_sorted_by_type[index_old : len(hands_sorted_by_type)] = sorted(hands_sorted_by_type[index_old : len(hands_sorted_by_type)], key=lambda hand: hand['card_points'])

# no completely sorted
#print(hands_sorted_by_type)
print("_---------------____---_-_---_-------------")

total_winnings = 0
for index, h_sorted in enumerate(hands_sorted_by_type):
    total_winnings += (index + 1) * int(h_sorted['bid'])
print(total_winnings)
