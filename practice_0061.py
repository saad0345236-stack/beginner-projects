# Practicing Drill:
import ctypes

word = 'Hi!'

for character in range(len(word), 0, -1):
    print(word[:character])

value_1 = 50
value_2 = 50

if value_1 == value_2:
    print("Same.")
else:
    print("Different.")

value_3 = "Apple"
value_4 = "Apple"

address_1 = hex(id(value_3))
address_2 = hex(id(value_4))

if address_1 == address_2:
    print("Same.")
else:
    print("Different.")

entry = input("Input: ")
new_entry = entry

print(new_entry.upper())