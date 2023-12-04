# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
data = []
# {'nr': , 'red': 0, 'blue': 0, 'green': 0}
colors = ['red', 'blue', 'green']
hyp_set = {'red': 12, 'blue': 14, 'green': 13}
with open("my_input2", "r") as f:
    while x := f.readline():
        x = x.rstrip() # remove crlf stuff on right side
        game_nr_str, game_data = x.split(":")
        game_nr = int(game_nr_str.split(" ")[1])
        res_dict = {'nr': game_nr, 'red': 0, 'blue': 0, 'green': 0}
        sets = game_data.split(";")
        for s in sets:
            elements = s.split(",")
            for color in colors:
                for el in elements:
                    if color in el:
                        nr_of_cubes = int(el.strip().split(' ')[0])
                        if res_dict[color] < nr_of_cubes:
                            res_dict[color] = nr_of_cubes
        data.append(res_dict)
print(data)

valid_games_summed = 0
for d in data:
    for c in colors:
        if d[c] > hyp_set[c]:
            print(f"impossible! {d[c]} {c} cubes revealed but only {hyp_set[c]} available")
            break
    else:
        print(f"valid game found: {d['nr']}")
        valid_games_summed += d['nr']
print(f"solution: {valid_games_summed}")

tmp = {'red': 0, 'blue': 0, 'green': 0}
sub_total = 0
for d in data:
    res = d['red'] * d['blue'] * d['green']
    print(f"powaaaaaa: {res}")
    sub_total += res
print(sub_total)