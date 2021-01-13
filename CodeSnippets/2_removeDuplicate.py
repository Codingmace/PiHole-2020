# Already known sorted domains.txt
a = open("sorted.txt", "r")
b = open("unique.txt", "w") # The new shorter list
c = open("dipli.txt", "w") # Duplicate ones that are detected
lines = a.readlines()
a.close()
# lines.sort() # Already Sorted
fir = 0 # First Value
sec = 1 # Comparing value
lim = len(lines) # Limit AKA number of lines
while(sec < lim):
    if(lines[fir] == lines[sec]): # Same keep going
        c.write(lines[sec])
        sec = sec + 1
    else: # Not the same
        b.write(lines[fir])
        fir = sec
        sec = fir + 1
b.write(lines[len(lines)-1]) # for the last element
b.close()
c.close()
#print(len(lines))
#for i in range(len(lines)-1):
#    print(lines[i] == lines[i+1])
#    if(i % 10 == 0):
#        i *= len(lines) - 5
# a.close()

# b.close() # not needed yet
