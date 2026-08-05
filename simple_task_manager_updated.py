# Updating the To Do List:
try:
    app = []
    order = 0
    while True:
        added = input("Add task: ")
        app.append(added)
        delete = input("Want to delete something? (y/n): ").lower()
        if delete == 'y':
            ask = input("What? ")
            app.remove(ask)
        else:
            pass
        mark = input("Do you want to mark a task as done? (y/n): ").lower()q
        if mark == 'y':
            task = int(input("Which one (index)? "))
            app[task] = [app[task] + '(DONE)']
        else:
            pass
        ask = input("Do you want to add another task? (y/n): ").lower()
        if ask == 'n':
            break
        else:
            pass
    for number, task in enumerate(app,start=1):
        number = str(number) + '.'
        print(number, task)
except ValueError:
    print("Invalid answer. Try again.")