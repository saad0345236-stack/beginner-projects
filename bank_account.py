# Creating a 'bank' type:
try:
    class Bank:
        def __init__ (self, amount_stored):
            self.amount_stored = amount_stored
        def withdraw(self, withdrawn):
            print(f"You have successfully withdrawn ${withdrawn}.")
        def deposit(self, deposits):
            print(f"Deposit completed. You have successfully deposted ${deposits}.")
    print("Welcome to the bank. Choose one of the options below:")
    digit = int(input("What's your current amount stored? "))
    bank = Bank(digit)
    print(f"Your current amount stored is ${bank.amount_stored}")
    ask = input("Would you like to 'withdraw' or 'deposit'? ").lower()
    if ask == "withdraw":
        withdrawn = int(input("Enter amount: "))
        bank.withdraw(withdrawn)
    elif ask == "deposit":
        deposits = int(input("Enter amount: "))
        bank.deposit(deposits)
    else:
        print("Invalid answer.")
except ValueError:
    print ("Invalid.")