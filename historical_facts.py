# Writing about a historical fact:
ask = input("Are you ready for historical fact? It's about how long WW2 lasted. Do you want to know? ")
if ask.upper() == "YES":
    print("WW2 lasted from 1939 to 1945.")
elif ask.upper() == "NO":
    print("Okay.")
else:
    print("Invalid answer.")
asking_again = input("Want to know another fact? ")
if asking_again.upper() == "YES":
    print("WW1 lasted from 1914 to 1918.")
elif asking_again.upper() == "NO":
    print("Okay.")
else:
    print("Invalid answer.")