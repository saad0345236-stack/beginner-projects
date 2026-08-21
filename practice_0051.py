# Practicing Drill:
vowels = 'aeiou'

sentence = input("Enter a sentence: ").lower()

vowel_count = 0

for letter in sentence:
    if letter in vowels:
        vowel_count += 1
        

print(f"Vowel Count: {vowel_count}")