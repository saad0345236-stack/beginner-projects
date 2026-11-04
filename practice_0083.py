# Practicing Session:
def names(**kwargs):
    print("Hi", end=" ")
    
    for key, value in kwargs.items():
        print(value, end=" ")

names(first="Jack", last="Smith")

animal = 'fox'
pet = 'dog'

print("The {} chased the {}".format(animal, pet))
print("The {1} chased the {0}".format(animal, pet))
print("The {animal} chased the {animal}".format(animal='fox', pet='dog'))

sentence = "The {} chases the {}."

print(sentence.format(animal, pet))