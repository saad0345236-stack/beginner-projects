# Practicing Session:
person = ('Sara', 25, 'Female')

print(person.count(25), person.index(25))

for x in person:
    print(x)

if 'Sara' in person:
    print("Her name is Sara.")

items = {'spoon', 'clock', 'pen', 'pencil'}
school_items = {'bag', 'eraser', 'pen'}

items.add('Notebook')
items.remove('spoon')

for x in items:
    print(x)

print(items.update(school_items))

random_items = items.union(school_items)

print(random_items)
print(school_items.difference(items))
print(items.intersection(school_items))

for x in random_items:
    print(x)