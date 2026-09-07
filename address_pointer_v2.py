# Address Pointer version 2:
def address(variable):
    location = hex(id(variable))
    value_id = id(variable)
    value_type = type(variable)

    return f"Value: {variable}. Address: {location}. ID: {value_id}. Type: {value_type}."

variable = input("Enter input: ")

print(address(variable))