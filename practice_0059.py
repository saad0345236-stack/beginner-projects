# Practicing Drill:
def same(a, b):
    if a > 0 and b > 0:
        if a == b:
            return True
            
        else:
            return False

    else:
        return "The values must be higher than 0."

try:
    a = int(input("What's A? "))
    b = int(input("What's B? "))
    
    print(same(a, b))

except ValueError:
    print("You can only enter positive integers.")