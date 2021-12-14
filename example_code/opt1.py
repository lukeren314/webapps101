# code readability

# Bad Example
def get_num(nums):
    return min(((nums[0].x-nums[0].y)**2+(nums[1].x-nums[1].y)**2)**0.5, 350)





























# Good Example
MAX_DISTANCE = 350

def get_distance(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

def get_truncated_distance(points):
    point1, point2 = points
    distance = get_distance(point1, point2)
    return min(distance, MAX_DISTANCE)



# Better Example
MAX_DISTANCE = 350

def get_distance(point1: tuple, point2: tuple) -> float:
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

def get_truncated_distance(points: tuple) -> float:
    point1, point2 = points
    distance = get_distance(point1, point2)
    return min(distance, MAX_DISTANCE)