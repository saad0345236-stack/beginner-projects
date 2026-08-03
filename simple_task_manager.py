# To Do List app version 1:
app = []
while True:
    added = input("Add task: ")
    app.append(added)
    print(app)
    delete = input("Want to delete something? (y/n): ").lower()
    if delete == 'y':
        ask = input("What? ")
        app.remove(ask)
        print(app)
    else:
        pass
    mark = input("Do you want to mark a task as done? (y/n): ").lower()
    if mark == 'y':
        task = int(input("Which one (index)? "))
        app[task] = [app[task] + '✓']
        print(app)
    else:
        pass
    ask = input("Do you want to add another task? (y/n): ").lower()
    if ask == 'n':
        break
    else:
        pass
print(app)