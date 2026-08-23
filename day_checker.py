# Day checker:
import datetime

day = datetime.date.today().strftime("%A")

question = input("Do you want to know the day? (y/n): ").lower()

if question == 'y':
    print(f"Today is a {day}.")

elif question == 'n':
    print("Understood.")

else:
    print("Sorry, I don't understand that.")