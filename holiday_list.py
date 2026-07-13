print("Let's create a list of your top 3 favorite holidays. Please enter any 3 holidays below:")
holiday_1 = input("1st Entry: ")
holiday_2 = input("2nd Entry: ")
holiday_3 = input("3rd Entry: ")
print("Good choices!")
question = input("Do you want to see the list? ").lower()
if question == "yes":
    print("This is your list:")
    print(f"1. {holiday_1}")
    print(f"2. {holiday_2}")
    print(f"3. {holiday_3}")
elif question == "no":
    print("That's fine. Have a nice day!")
else:
    print("Sorry, I don't understand that.")