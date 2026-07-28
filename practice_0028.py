# Practicing fizz_buzz:
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input
print("Enter a number:")
ask = int(input(">"))
print(fizz_buzz(ask))