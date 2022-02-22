word1 = input()
word2 = input()

# How many letters does the longest word contain?

word1len = len(word1)
word2len = len(word2)

if word1len > word2len:
    print(word1len)
else:
    print(word2len)
