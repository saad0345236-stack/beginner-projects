# Generating a sentence:
first_name = 'Jake'
last_name = 'Robertson'
sentence = first_name + " [" + last_name + "] is from France."
print(sentence)
# Cleaning up the code:
new_sentence = f'{first_name} [{last_name}] is from France & speaks French.'
print(new_sentence)
# Practing with methods, functios & operators:
language = "Jake speaks French"
print(len(language))
print(language.upper())
print(language.lower())
print(language.find('French'))
print(language.replace('French', 'English'))
print(language.title())
print('Jake' in language)
print('jake' in language)