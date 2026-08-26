# Practicing Drill:
string = input("Enter string: ").lower()

non_repeating = []
repeating = []

for character in string:
    if string.count(character) > 1:
        if character not in repeating:
            repeating.append(character)
    
    else:
        non_repeating.append(character)

print(f"Repeating Characters: {repeating}")
print(f"Non–Repeating Characters: {non_repeating}")