# Converting digits into words:
print("Enter any digits of your choice below and they'll be converted to words.")
digits = input("Digits: ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
result = ''
for digit in digits:
    result += numbers.get(digit, "!") + ' '
print(result)
# Practing return statements in functions:
def times_3(digit):
    print(digit * 3)
    return
times_3(3)