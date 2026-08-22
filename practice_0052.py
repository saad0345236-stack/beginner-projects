# Practicing Drill:
def incrypt(prompt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    encrypted = ''

    for letter in prompt:
        if letter in alphabet:
            new_prompt = (alphabet.index(letter) + 1) % 26

            encrypted += alphabet[new_prompt]
        
        else:
            encrypted += letter
    
    return encrypted

user_input = input("Enter a prompt: ").lower().strip()

print(incrypt(user_input))