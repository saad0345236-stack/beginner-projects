# Palindrome checker:
print("This is a palindrome checker.")

def palindrome(word):
    if word == word[::-1]:
        return "That is a palindrome!"
    
    else:
        return "That is not a palindrome."

word = input("Enter a word: ").lower()

print(palindrome(word))