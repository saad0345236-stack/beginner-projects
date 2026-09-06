# Address Pointer:
def address(variable):
    location = hex(id(variable))
    return location

variable = input("Enter input: ")

print(address(variable))