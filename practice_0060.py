# Practicing Drill:
import ctypes

address = 50
print(hex(id(address)))

value = ctypes.c_int(99)
pointer = ctypes.pointer(value)

print(f"Pointer: {pointer}")
print(f"Value at address: {pointer.contents.value}")

address_2 = 'str'
print(hex(id(address_2)))

for char in address_2:
    location = hex(id(char))
    print(f"Character: {char}")
    print(f"Location {location}")

character = ctypes.c_char(b"A")
char_ptr = ctypes.pointer(character)
print(char_ptr.contents.value)