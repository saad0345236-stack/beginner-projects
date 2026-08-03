# Practicing lists:
words = []
count = 0
user_count = int(input("> "))

while count <= user_count:
    entry = input("> ")
    words.append(entry)
    count += 1

print(words)