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
        for line in f:
            if random() < 0.5:
                random_lines.append(line)
                break
    return random_lines



# Bad Example
def check_important_items(items, isimportant):
    important_items = []
    for item in items:
        if isimportant(item) and item not in important_items:
            important_items.append(item)
    return important_items



# Good Example (sometimes)
def check_important_items(items, isimportant):
    important_items = set()
    for item in items:
        if isimportant(item):
            important_items.add(item)
    return important_items