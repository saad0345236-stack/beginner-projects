# Practicing Drill:
print("Welcome to our convenience store.")

try:
    price = float(input("Enter the price of an item: "))

    membership = input("Do you have a membership? (y/n): ").lower()
    
    if membership == 'y' and price >= 100.00:
        discount_1 = price * 0.25
        final_price = price - discount_1
        print(f"You get a 25% discount. The final price is ${final_price:.2f}")
    
    elif membership == 'y' or price >= 100.00:
        discount_2 = price * 0.15
        final_price = price - discount_2
        print(f"You get a 15% discount. The final price becomes ${final_price:.2f}.")
    
    else:
        print(f"There isn't any discount for you. The final price is ${price:.2f}.")

except ValueError:
    print("Enter a positive number.")