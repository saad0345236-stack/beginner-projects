# Threshold Validator:
def threshold(value, minimum=None):
    while True:
        try:
            entry = int(input(value))
            if minimum is not None and entry <= minimum:
                print("Value is less than minimum.")
                continue
            return entry

        except ValueError:
            print("Enter integer.")

user_choice = int(input('>'))
checker = threshold("Enter answer: ", user_choice)