# Robustness


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



# Bad Example 2
def min_distance(points, target_point):
    min_point = None
    for point in points:
        if min_point is None or ((point.x - target_point.x)**2 + (point.y - target_point.y)**2)**0.5 < ((min_point.x - target_point.x)**2 + (min_point.y - target_point.y)**2)**0.5:
            min_point = point
    return ((min_point.x - target_point.x)**2 + (min_point.y - target_point.y)**2)**0.5



# Good Example 2 (halfway)
def distance(point, target_point):
    return ((point.x - target_point.x)**2 + (point.y - target_point.y)**2)**0.5

def min_distance(points, target_point):
    min_point = None
    for point in points:
        if min_point is None or distance(point, target_point) < distance(min_point, target_point):
            min_point = point
    return distance(min_point, target_point)



# Good Example 2
def distance(point, target_point):
    return ((point.x - target_point.x)**2 + (point.y - target_point.y)**2)**0.5

def min_distance(points, target_point):
    min_distance = None
    for point in points:
        point_distance = distance(point, target_point)
        if min_distance is None or point_distance < min_distance:
            min_distance = point_distance
    return min_distance
