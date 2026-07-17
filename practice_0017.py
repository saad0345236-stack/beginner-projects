# Removing duplicates from a list:
numbers = [1, 1, 3, 3, 6, 6]
new_list = []
for number in numbers:
    if number not in new_list:
        new_list.append(number)
print(new_list)
# Practicing tuples:
tuple_1 = (1, 3, 5, 7, 3)
print(tuple_1.count(3))
print(tuple_1[2])
# Practicing unpacking:
tuple_2 = (3, 5, 6, 8, 10)
v, w, x, y, z = tuple_2
print(w)
list_1 = [2, 7, 3, 10]
a, b, c, d = list_1
print(a, b, c, d)
# Creating a dictionary:
diary = {
    "name": "Chris",
    "age": 21,
    "is_adult": True,
    "birthday": "27th June"
}
print(diary.get("country"))
print(diary.get("profession", "doctor"))
diary["age"] = 22
print(diary.get("age"))
diary["has_degree"] = True
print(diary.get("has_degree"))