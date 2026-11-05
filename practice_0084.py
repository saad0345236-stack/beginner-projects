# Practicing Session:
import random

x = random.randint(1, 6)
y = random.random()
picks = ['rock', 'paper', 'scissor']
chars = [0,1,2,3,4,'A','B']
shuffled = random.shuffle(chars)

print(x, y, random.choice(picks))
print(shuffled)

answer = 4.12345
number = 1000

print("2 + 2 is {}".format(answer))
print("2 + 2 is {0:10}, when you add both values".format(answer))
print("2 + 2 is {:<10}, when you add both values.".format(answer))
print("2 + 2 is {:>10}, when you add both values.".format(answer))
print("2 + 2 is {:^10}, when you add both values.".format(answer))

print("The answer is {:.2f}".format(answer))
print("The answer is {:.3f}".format(answer))
print("The answer is {:,}".format(number))
print("The answer is {:b}".format(number))
print("The answer is {:x}".format(number))
print("The answer is {:e}".format(number))
print("The answer is {:o}".format(number))