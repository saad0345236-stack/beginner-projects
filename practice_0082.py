# Practicing Session:
number = 5

def digit():
    # number = 4
    print(number)

print(number)
digit()

def add(*args):
    total = 0
    args = list(args)
    args[1] = 0
    
    for i in args:
        total += i
    
    return total

print(add(5, 5, 5))