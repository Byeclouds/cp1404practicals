"""
Word Occurrences
Estimate: 20 minutes
Actual:   18 minutes
"""

word_count = {}
user_input = input("Text:")

give_words = user_input.split()
for word in give_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

give_words = list(word_count.keys())
give_words.sort()

word_max_length = max((len(word) for word in give_words))
for word in give_words:
    print(f"{word:{word_max_length}} : {word_count[word]}")
