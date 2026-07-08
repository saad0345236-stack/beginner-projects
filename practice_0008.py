# Exercise:
name_length = int(input("No. of characters in your name: "))
if name_length < 3:
    print("Name shouldn't contain less than 3 characters.")
elif name_length > 50:
    print("Name shouldn't exceed 50 characters.")
else:
    print("Name looks good.")
# Another Exercise:
ask = int(input("Weight: "))
ask_2 = input("Is in pounds? ")
if ask_2.upper() == "YES":
    print(f"You're {ask} pounds.")