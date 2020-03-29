s = input()
word1 = s[:s.find(' ')]
word2 = s[s.find(' ') + 1:]
print(word2+ ' ' + word1)