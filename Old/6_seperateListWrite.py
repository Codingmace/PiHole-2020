

# Already known sorted unique.txt
a = open("unique.txt", "r") # The new shorter list
b = open("basic.txt", "w") # Left Over when seperated
c = open("sexy.txt","w") # Sexy playlist of words
d = open("keySwords.txt","r") # Key words for the sex domain List
lines = d.readlines()
keyWord1 = ''
for line in lines:
    keyWord1 += line.split()
    
