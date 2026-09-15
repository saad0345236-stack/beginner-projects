# Practicing Drill:
numbers = [1, 2, 3, 4, 5]

try:
    search = int(input("Search for a numher: "))

    if search in numbers:
        print(True)
    
    else:
        print(False)

except ValueError:
    print("You can only search for integers.")