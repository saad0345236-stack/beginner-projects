# Making an emoji converter:
print("Enter one of these faces with some text: :), :( & ;)")
def get_emoji(message):
    text = message.split(" ")
    emojis = {
        ':)': '😊',
        ':(': '☹️',
        ';)': '😉'
    }
    result = ''
    for item in text:
        result += emojis.get(item, item) + ' '
    return result
message = input(">")
print(get_emoji(message))
# Practicing with 'class':
class Number:
    def help(self):
        print("Help!")
    def stop(self):
        print("Stop")
number1 = Number()
number1.x = 28
print(number1.x)
number1.stop()
number2 = Number()
number2.y = 33
print(number2.y)
number3 = Number()
number3.z = 292
print(number3.z)
number3.help()
class Digits:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
digit = Digits(33, 66, 99)
digit.y = 65
print(digit.y, digit.z)