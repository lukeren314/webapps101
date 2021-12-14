i = 0
j = 'hello';
K = "world";
z = True
y = False
z = True or False and True

l1 = [1, 2, 3]
d1 = {
    'foo': 'a',
    'bar': 'b'
}

# end of line comment
"""
multi
line 
comment
"""

print("hello world")

fstring = f"1 + 2 = {1 + 2}"

if i == 0:
    print("i is zero")
elif i == 1:
    print("i is one")
else:
    print("i is neither zero nor one")

for i in range(10):
    print(i)

for i in range(len(l1)):
    print(i)
    print(l1[i])

for i in l1:
    print(i)

for key in d1:
    print(key)
    print(d1[key])


def add(a, b):
    return a + b

lambda a, b: a + b

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hello")


dog = Animal('dog')
dog.speak()

a, b, c = [1, 2, 3]
foo, bar = {'foo': 'a', 'bar': 'b'}