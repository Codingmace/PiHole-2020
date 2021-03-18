import re

pattern = re.compile("^adtrack(er|ing)?[0-9]*[_.-]")

# f = open("Unique1.txt", 'r')
g = open("filtered.txt", "w")
h = open("patterns.txt", "r")
i = open("removed.txt", "w")
lines = []
numb = 0
bamb = True
with open('Unique1.txt') as openfileobject:
    while bamb:
        print(numb)
        if numb > 400000:
            break
        try:
            for y in openfileobject:
                if("#" in y or "!" in y or "*" in y or "[" in y or "]" in y or "?" in y):
                    y = " " # Ignore
                else:
                    lines.append(y)
                    #print(numb)
                    numb += 1
        except:
            print("")
        
            

"""
while not f.eof():
    y = f.readline()
    if("#" in y or "!" in y or "*" in y or "[" in y or "]" in y or "?" in y):
        # Ignore
        y = " "
    else:
        lines.append(y)
# lines = f.readlines()
f.close()
"""
lines2 = []
a = h.readlines()
h.close()
"""
patterns = []

for l in a:
    patterns.append(re.compile(l))

"""
counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
patterns = [re.compile('^adtrack(er|ing)?[0-9]*[_.-]'),
            re.compile('^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]\n'),
            re.compile('^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]\n'),
            re.compile('^(.+[_.-])?telemetry[_.-]\n'),
            re.compile('^adim(age|g)s?[0-9]*[_.-]\n'),
            re.compile('^adtrack(er|ing)?[0-9]*[_.-]\n'),
            re.compile('^advert(s|is(ing|ements?))?[0-9]*[_.-]\n'),
            re.compile('^aff(iliat(es?|ion))?[_.-]\n'),
            re.compile('^analytics?[_.-]\n'),
            re.compile('^banners?[_.-]\n'),
            re.compile('^beacons?[0-9]*[_.-]\n'),
            re.compile('^count(ers?)?[0-9]*[_.-]\n'),
            re.compile('^mads\\.\n'),
            re.compile('^pixels?[-.]\n'),
            re.compile('^stat(s|istics)?[0-9]*[_.-]')]
print(patterns)
for line in lines:
    matches = False
    b = 0
    for pat in patterns:
        if(pat.match(line)):
            matches = True
            counts[b] = counts[b] + 1
        b = b + 1
    if(matches):
        i.write(line)
    else:
        g.write(line)
        lines2.append(line)
i.close()
g.close()
for q in counts:
    print(q)
#for line in lines2:
#    print(line)
