import re

# Already known sorted unique.txt
a = open("unique.txt", "r") # The new shorter list
b = open("words.txt", "w") # Each word
c = open("counts.txt","w") # Counting of each word
lines = a.readlines()
a.close()
wordList = ""
for line in lines:
    result = re.sub('[\W_]+', ' ', line)
    wordList += result + " "
    print(result)
print(len(wordList.split()))
words = wordList.split()
words.sort()
for word in words: # Writting a check point file of NonAlphaNumeric words
    b.write(word)
b.close()
limit = len(words)
i = 0
while(i < limit):
    count = 0
    j = i+1
    if (j >= limit -25):
        break
    while(words[i] == words[j]): # Keep counting while they match
        count = count + 1
        j = j + 1
    c.write(words[i]+ " " + str(count) + "\n")
    i = j
c.close()
