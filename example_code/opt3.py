# Robustness



# Bad Example
def is_cute_animal(thing):
    if thing == "cat":
        return True
    elif thing == "dog":
        return True
    else:
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Good Example 1
def is_animal(thing):
    if thing == "cat":
        return True
    if thing == "dog":
        return True
    return False
    

    
    
    
    
    
    
    
    
    
    
    
# Good Example 3
animals = set('dog', 'cat')
    
def is_animal(thing):
    return thing in animals


# Bad Example
def min_distance(points, target_point):
    min_point = None
    for point in points:
        if min_point is None or ((point.x - target_point.x)**2 + (point.y - target_point.y)**2)**0.5 < ((min_point.x - target_point.x)**2 + (min_point.y - target_point.y)**2)**0.5:
            min_point = point
    return ((min_point.x - target_point.x)**2 + (min_point.y - target_point.y)**2)**0.5

















# Good Example (halfway)
def distance(point, target_point):
    return ((point.x - target_point.x)**2 + (point.y - target_point.y)**2)**0.5

def min_distance(points, target_point):
    min_point = None
    for point in points:
        if min_point is None or distance(point, target_point) < distance(min_point, target_point):
            min_point = point
    return distance(min_point, target_point)


















# Good Example
def distance(point, target_point):
    return ((point.x - target_point.x)**2 + (point.y - target_point.y)**2)**0.5

def min_distance(points, target_point):
    min_distance = None
    for point in points:
        point_distance = distance(point, target_point)
        if min_distance is None or point_distance < min_distance:
            min_distance = point_distance
    return min_distance





