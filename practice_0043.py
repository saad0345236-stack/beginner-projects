# Practicing drills:
import datetime
print(datetime.datetime.now())
product = {
    'I1': {
        "name": "apple",
        "price": 100.0,
        "quantity": 5,
        "date": datetime.datetime.now()
    }
}
I1_dict = product.get("I1")
print(product['I1']['date'])

def pause():
    return 'Paused'
print(pause())

def word(prompt):
    while True:
        result = input(prompt)
        if result:
            return result
        print("Input cannot be empty.")
word('Enter prompt: ')