# Practicing drill:
animals = ['Cheetah', 'Panda', 'Snake']
animals.append('Lion')
animals.append('Elephant')
number = int(input("Which task should be deleted by number? "))
animals.pop(number - 1)
favorite_animal = int(input('Which animal is your favorite? (number): '))
animals[favorite_animal - 1] += '(FAVORITE)'
edited_animal = int(input('Which animal do you want to replace? (number): '))
replace = input('What is the replacement? ')
animals[edited_animal - 1] = replace

for number, animal in enumerate(animals, start=1):
    number = str(number) + '.'
    print(number, animal)

try:
    safe_number = int(input('Enter number: '))
    print('You entered:', safe_number)
except ValueError:
    print('It must be an integer.')