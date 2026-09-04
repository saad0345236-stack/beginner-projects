# Practicing Drill:
def swap(value_1, value_2):
    temp = value_1
    value_1 = value_2
    value_2 = temp

    return value_1, value_2

x = 1
y = 2

print(swap(x, y))

phone_book = {'Kelly': "342-463-1000", 'Joe': "453-757-1000"}
phone_book["James"] = "436-433-1000"

print(phone_book["Kelly"])
print(phone_book)