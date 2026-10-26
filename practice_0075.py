# Practicing Session:
for i in range(11):
    print(i)

for i in range(10, 21, 2):
    print(i)

temp = int(input("What's the temperature today? "))

if temp >= 0 and temp <= 30:
    print("Weather is nice today!")
elif temp < 0:
    print("The weather seems cold today!")
elif not (temp < 30):
    print("Weather seems very hot today!")
else:
    print("Invalid answer.")

name = None

while not name:
    name = input("Enter name: ")

print("Hello,", name)