# Project 4 — Word Counter
# Author: MNC

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# total word count
total_words = len(words)

# character count (no spaces)
total_characters = len(sentence.replace(" ", ""))

# word frequency dictionary
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# print results
print(f"\nTotal words: {total_words}")
print(f"Total characters (no spaces): {total_characters}")

print("\nWord frequency:")
for word in frequency:
    print(f"{word}: {frequency[word]}")
