
# Using readline() 
file1 = open('MergeLogs.txt', 'r')
file2 = open("BlockedLogs.txt", "w")
count = 0
firstWord = "blocked "
secondWord = " is "
while True: 
    count += 1
  
    line = file1.readline()
#    print(line)
    if firstWord in line and secondWord in line:
        firstIndex = line.index(firstWord)
        secondIndex = line.index(secondWord)
#        print(line)
        addr = line[firstIndex+len(firstWord):secondIndex]
        #print(addr)
        file2.write(addr+ "\n")
    # if line is empty 
    # end of file is reached 
    if not line: 
        break

file2.close()
file1.close() 
