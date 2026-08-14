# Practicing Drill:
def digit(entry, minimum=None):
    while(True):
        try:
            answer = int(input(entry))
            if minimum is not None and answer <= minimum:
                print("Enter an integer higher than 10.")
                continue
            return answer
        except ValueError:
            print("You can only enter integers.")

user_input = digit("Enter a number which is higher than 10: ", 10)

print(f"Answer accepted: {user_input}!")