# Converting brackets and colons into emojis:
emoji = input("Enter either ':)' or ':(' after the colon with any message of your choice: ")
message = emoji.split(' ')
emoji_book = {
":)": "☺️",
":(": "☹️"
}
output = ""
for item in message:
    output += emoji_book.get(item, item) + ' '
print(output)
# Defining a function:
def greet():
    print("Hi!")
    print("Nice to meet you.")
print("Starting")
greet()
print("Finished")
# Adding arguements to function:
def welcome(first_name, last_name):
    print(f"Hi! Welcome {first_name} {last_name}!")
    print("It's nice to have you.")
print("Function called below:")
welcome("Jacob", "Smith")
print("Message displayed above.")
# Using keyword arguments:
def numbers(first_digit, second_digit):
    print(f"{first_digit}, {second_digit}")
numbers(second_digit="2", first_digit="1")