# Final version of the To Do List:
try:
    app = []
    order = 0
    while True:
        added = input("Add task: ")
        app.append(added)
        delete = input("Want to delete something? (y/n): ").lower()
        if delete == 'y':
            ask = int(input("What? (1 based number): "))
            app.pop(ask - 1)
        else:
            pass
        mark = input("Do you want to mark a task as done? (y/n): ").lower()
        if mark == 'y':
            task = int(input("Which one (1 based number)? "))
            app[task - 1] = app[task] + '(DONE)'
        else:
            pass
        edit = input("Do you want to edit a task? (y/n): ").lower()
        if edit == 'y':
            editing = int(input("Which one? (1 based number): "))
            change = input("To what? ")
            app[editing - 1] = change
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