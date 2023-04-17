text = input("Text: ")
words = text.split()  # split the string into a list of words
word_to_occurrences = {}  # create an empty dictionary

for word in words:  # for each word in the list of words
    frequency = word_to_occurrences.get(word, 0)
    word_to_occurrences[word] = frequency + 1

words = list(word_to_occurrences.keys())  # get a list of the keys (words)
words.sort()

max_length = max((len(word) for word in words))  # get the length of the longest word
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_occurrences[word]))
