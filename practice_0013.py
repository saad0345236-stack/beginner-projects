# Updating a car game:
started = False
while True:
    menu = input("> ").lower()
    if menu == "help":
        print("""
Start – starts the car
Stop – stops the car
Quit – quits the game
        """)
    elif menu == "start":
        if started:
            print("Car already started.")
        else:
            print("Car started.")
            started = True
    elif menu == "stop":
        if not started:
            print("Car already stopped.")
        else:
            print("Car stopped.")
            started = False
    elif menu == "quit":
        break
    else:
        print("I don't understand that...")
# Calculating total costs from a list:
costs = [10, 20, 30]
total = 0
for cost in costs:
    total += cost
print(f"Total: {total}")