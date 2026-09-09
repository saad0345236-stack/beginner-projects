# Address Pointer version 3:
def address(value):
    location = hex(id(value))
    value_id = id(value)
    value_type = type(value)

    return f"Value: {value}. Address: {location}. ID: {value_id}. Type: {value_type}."

value = input("Enter input: ")

print(address(value))

while True:
    choice = input("Do you want to input another prompt? (y/n): ").lower()

    if choice == 'y':
        value = input("Enter input: ")
        print(address(value))
    
    elif choice == 'n':
        print("Understood.")
        break
    
    else:
        print("Sorry, I don't understand that.")