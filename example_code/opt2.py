# Efficiency

from random import random

# Bad Example
def pick_random_lines(filename, num_samples):
    random_lines = []
    for _ in range(num_samples):
        with open(filename) as f:
            for line in f:
                if random() < 0.5:
                    random_lines.append(line)
                    break
    return random_lines

























# Good Example (sometimes)
def pick_random_lines(filename, num_samples):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line)
    random_lines = []
    for _ in range(num_samples):
        for line in lines:
            if random() < 0.5:
                random_lines.append(line)
                break
    return random_lines














# Bad Example 1
def find_min_score_player(players):
    min_player = None
    for player in players:
        if min_player is None:
            min_player = player
        elif min_player is not None and player.score < min_player.score:
            min_player = player
    return min_player





















# redundancy examples
a = True
b = False
def foo():
    pass
def bar():
    pass


if a:
    foo()
elif not a:
    bar()



if a:
    foo()
else:
    bar()



if a:
    foo()
elif b:
    foo()



if a or b:
    foo()




if a:
    foo()
elif not a and b:
    foo()



# Good Example 1
def find_min_score_player(players):
    min_player = None
    for player in players:
        if min_player is None or player.score < min_player.score:
            min_player = player
    return min_player

