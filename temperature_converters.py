# Temperature converters:
choice = input("C to F or F to C? ").lower()
if choice == 'c to f':
    c = float(input('Celsius: '))
    print(f"F is {(c * 9/5) + 32}")
elif choice == 'f to c':
    f = float(input('Fahrenheit: '))
    print(f"C is {(f - 32) * 5/9}")
else:
    print("your choice is invalid.")