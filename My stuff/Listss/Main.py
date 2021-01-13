import dns.resolver
import os.path

debug = True

def get_records(domain):
    ids = ['A', 'AAAA', 'SOA', 'CNAME', 'MX', 'NS', 'PTR', 'CERT', 'SRV', 'TXT']
    
    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                return a            
        except Exception as e:
            print(e)  # or pass
    return "NA"


def validation(filename):
    a = open(filename, "r") # The current file
    b = open("valid.txt", "w") # For the shorter valid types
    if (debug):
        c = open("invalid.txt", "w") # For the shorter invalid types
    lines = a.readlines()
    lines.sort()
    a.close()
    for line in lines:
        ans = get_records(line)
        if (!(ans == "NA")):
            b.write(line)
        elif (debug):
            c.write(line)
            
    b.close()
    if (debug):
        c.close()

def removeDuplicates(filename):
    a = open(filename, "r")
    b = open("unique.txt", "w") # The new shorter list
    if(debug):
        c = open("dipli.txt", "w") # Duplicate ones that are detected
    lines = a.readlines()
    a.close()
    fir = 0 # First Value
    sec = 1 # Comparing value
    lim = len(lines) # Limit AKA number of lines
    while(sec < lim):
        if(lines[fir] == lines[sec]): # Same keep going
            if(debug):
                c.write(lines[sec])
            sec = sec + 1
        else: # Not the same
            b.write(lines[fir])
            fir = sec
            sec = fir + 1
    b.write(lines[len(lines)-1]) # for the last element
    b.close()
    if(debug):
        c.close()

""" CAN'T GET THIS FUCKING THING WORKING """
def subFiles(foldPath):
    # walk the folder for files
    """ GOING TO THE DEFAULT OF FOLDER SEPERATING BECAUSE I CANT GET THE OTHER THING TO WORK"""
    fileList = []
    foldPath = "Seperating\\"
    folderpath = os.listdir(foldPath)
    for f in folderpath:
        if (os.path.isfile(f)):
            fileList.append(f)
    print(fileList)

def merger(files):
    # Merge the files together into one
    
    

def mergeFiles(foldername):
    # Walk the path of the files
    fileList = subFiles(foldername)
    # Merge the files together
    merger(fileList)
    
    filename = "valid.txt" # The merged file name
    


def main():
    print("Let us start this out with a few questions")
    print("What do we want to do. Keep in mind 3 can also do steps 1 and 2")
    print("1. Validate List\n2. Merge List, Sort, and remove duplicates")
    print("3. Split up the list\n4. Crawl for new list")
    selection = input()
    if(selection == 1):
        print("Awesome you are going easy on me. All I need you to do is enter the path of the file and we will be on our way")
        filepath = input()
        validation(filepath)
        print("Ok that is it. I am done")
    if(selction == 2):
        print("Ok, a little bit of work but still easy.")
        print("I need you to now input the folder path")
        foldPath = input()
        newFilename = "mergedList.txt"
        mergeFiles(foldPath)
        doValid = input("Just making sure, do you want to validate (Yes/No): ")
        if (doValid == "Yes"):
            print("Ok validating")
            validation("valid.txt")
        else:
            print("Awesome, no validation")
        print("Removing Duplicates")
        removeDuplicates("valid.txt")
        print("Ok we are all done. The requested file is named unique.txt")
    if (selection == 3):
        print("Picky one are we. I want to make sure that we are not going to waste time")
        firstStep = input("Do you want to merge any files (Yes/No): ")
        currentFile = "" # Name of the file reading from
        if (firstStep == "Yes"):
            foldPath =input("Enter the folder path: ")
            mergeFiles(foldPath)
            currentFile = "valid.txt"
        else:
            filepath =input("Enter the file path: ")
            currentFile = filepath

        removeDuplicates(currentFile)
        currentFile = "unique.txt"
        
        secondStep = input("Do you want to validate the entries (Yes/No): ")
        if (secondStep == "Yes"):
            print("Dang it you are making me do so much work")
            validation(currentFile)
        else:
            print("Ok. That will make things go quicker")

        print("Now for the seperation. I bet you don't know what you want to seperate by.")
        print("I will make it easy and give you some options")
        
        
        foldPath = input("Enter in the folder with the files")
        
    if (selection == 4):
        print("Oh my, you want the hardest thing. I haven't programmed that far so I will let you answer some more questions.")
        firstStep = input("Do you want to merge any files (Yes/No): ")
        currentFile = "" # Name of the file reading from
        if (firstStep == "Yes"):
            foldPath =input("Enter the folder path: ")
            mergeFiles(foldPath)
            currentFile = "valid.txt"
        else:
            filepath =input("Enter the file path: ")
            currentFile = filepath

        removeDuplicates(currentFile)
        currentFile = "unique.txt"
        
        secondStep = input("Do you want to validate the entries (Yes/No): ")
        if (secondStep == "Yes"):
            print("Dang it you are making me do so much work")
            validation(currentFile)
        else:
            print("Ok. That will make things go quicker")

        print("Sucks if you want to seperate the files. That is your punishment for choosing an advanced thing.")
        print("Rerun the program if you want to do Selection 3")

    print("Goodbye")


main()
