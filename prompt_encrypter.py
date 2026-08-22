# Prompt encrypter:
prompt = input("Enter prompt: ").lower().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypter = ''


for letter in prompt:
    if letter in alphabet:
        new_letter = (alphabet.index(letter) + 3) % 26

        encrypter += alphabet[new_letter]
    
    else:
        encrypter += letter

print(encrypter)