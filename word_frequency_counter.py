# Word frequency counter:
finding_duplicates = {}

sentence = input("Enter a sentence: ").lower()

for word in sentence.split():
    if word not in finding_duplicates:
        finding_duplicates[word] = 1
    else:
        finding_duplicates[word] += 1

print(finding_duplicates)