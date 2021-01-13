# Sorting the already known merged file domains.txt
a = open("sorted.txt", "w")
b = open("domains.txt", "r")
lines = b.readlines()
lines.sort()
for line in lines:
    a.write(line)
a.close()
b.close()
