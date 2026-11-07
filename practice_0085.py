# Practicing Session:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the dinominator: "))

    answer = numerator / denominator

    print(answer)

except ZeroDivisionError:
    print("You can't divide by zero.")

except Exception:
    print("Error.")