# Practicing Session:
try:
    value_1 = int(input("Enter a number: "))
    value_2 = int(input("Enter a second number: "))

    answer = value_1 / value_2

    print(answer)

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero.")

except ValueError as e:
    print(e)
    print("You can only enter numbers.")

except Exception as e:
    print(e)
    print("Error.")

else:
    print(answer)

finally:
    print("Finished.")