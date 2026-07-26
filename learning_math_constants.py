# Giving user the value of pi, e or tau:
print("Enter a either 'pi', 'e' or 'tau' below to learn their first 10 values:")
choice = input(">").lower()
if choice == 'pi':
    print("The first 10 values of π are 3.141592653")
elif choice == 'e':
    print("The first 10 values of e are 2.718281828")
elif choice == 'tau':
    print("The first 10 values of tau are 6.283185307")
else:
    print("Invalid answer.")