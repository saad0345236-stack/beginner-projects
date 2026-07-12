# Exercise:
print("This is a car game. Type 'help' for options or start playing.")
while True:
    option = input("> ").lower()
    if option == "help":
        print("""
start = starts car
stop = stops car
quit = quits game
        """)
    elif option == "start":
        print("Car started.")
    elif option == "stop":
        print("Car stopped.")
    elif option == "quit":
        print("You've exited the game.")
        break
    else:
        print("I don't understand that.")