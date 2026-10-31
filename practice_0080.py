# Practicing Session:
person_name = "Jake Robertson"
first_name = person_name[:4].lower()
last_name = person_name[5:].upper()
last_letter = person_name[-1]

print(first_name, last_name, last_letter)

def introduction(name, age):
    print("It's so nice to meet you", name)
    print("You're", age, "years old.")

introduction(person_name, 23)