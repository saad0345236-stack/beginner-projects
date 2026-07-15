# Letting a user change 1 value in a matrix list:
the_list = [
    [3, 6, 9],
    [12, 15, 18],
    [21, 24, 27]
]
print(the_list)
print("Change any 1 value in the given list.")
row = int(input("Row index? "))
column = int(input("Column index? "))
change = int(input("What's the new value? "))
the_list[row][number] = change
print(the_list)