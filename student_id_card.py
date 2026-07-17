# Making a student ID card for the user with a dictionary:
print("We'll assign an ID card to you, but first you need to enter your information below:")
name = input("Name: ").capitalize()
age = input("Age: ")
grade = input("Class: ")
school = input("School Name: ")
id_card = {
"name": name,
"age": age,
"grade": grade,
"school": school
}
print(id_card["name"])
print(id_card["age"])
print(id_card["grade"])
print(id_card["school"])
question = input("Is this information correct? if yes, we'll print your card: ").lower()
if question == "yes":
    print("====================")
    print("  STUDENT ID CARD  ")
    print("====================")
    print("Name:", id_card["name"])
    print("Age:", id_card["age"])
    print("Grade:",
    id_card["grade"])
    print("School:", id_card["school"])
    print("====================")
elif question == "no":
    print("Try again.")
else:
    print("Invalid answer.")