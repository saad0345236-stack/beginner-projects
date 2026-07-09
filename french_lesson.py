# Teaching French counting from 1 to 10:
choice = input("Do you want to learn French counting? ")
if choice.upper() == "YES":
    print("First we need to write down our numbers, which are:")
    n = 1
    while n <= 10:
        print(n)
        n = n + 1
    confirming = input("Are you ready? ")
    if confirming.upper() == "YES":
        print("1 = Un")
        print("2 = Deux")
        print("3 = Trois")
        print("4 = Quatre")
        print("5 = Cinq")
        print("6 = Six")
        print("7 = Sept")
        print("8 = Huit")
        print("9 = Neuf")
        print("10 = Dix")
    else:
        print("Lesson stopped.")
else:
    print("Lesson stopped.")