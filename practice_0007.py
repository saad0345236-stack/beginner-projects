# Exercise:
house_cost = 1000000
good_credit = False
if good_credit:
    put_down = house_cost * 0.1
else:
    put_down = house_cost * 0.2
print(f"${put_down}")
# Logical Operators:
has_credit = True
is_criminal = False
if has_credit and not is_criminal:
    print("Eligible for loan.")
else:
    print("Not Eligible.")
# Comparaison Operators:
age = 17
if age > 17:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
# More practicing:
sentence = "I'm learning Python"
print(sentence[0:4])
print(sentence[:-1])