# Practicing Drill:
duplicated_list = ['a', 'b', 'b', 'a', 'c', 'd']
non_duplicates = []

for letter in duplicated_list:
    if letter not in non_duplicates:
        non_duplicates.append(letter)

print(non_duplicates)

sentence = 'Python is a case sensitive language and python is a programming language'

word_count = {}
name = 0

for word in sentence.lower().split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

print(word_count)