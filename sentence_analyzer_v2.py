# Sentence analyzer version 2:
def sentence_analyzer(sentence):
    words = sentence.split()

    utterance = []
    for word in words:
        utterance.append(word)
    
    total = len(utterance)
    longest = ''
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    result = f"Total number of words in the sentence are {total}. The largest word is {longest}. The sentence in all caps is '{sentence.upper()}' and sentence in lower caps is '{sentence.lower()}'."

    return print(result)

sentence = input("Enter sentence: ").lower()

sentence_analyzer(sentence)