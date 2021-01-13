import dns.resolver

a = open("un.txt", "r") # For checking DNS while other one runs
b = open("types.txt", "w") # Checking the Types are valid
c = open("invalidTypes.txt", "w") # Writing the invalid ones
d = open("validTypes.txt", "w") # For the shorter valid types
lines = a.readlines()
for line in lines:
    try:
        answer = dns.resolver.resolve(line)
        rdt = dns.rdatatype.to_text(answer.rdtype)
        b.write(rdt)
        d.write(line)
    except:
        c.write(line)
        print(line + " is not valid")
        
b.close()
c.close()
d.close()
