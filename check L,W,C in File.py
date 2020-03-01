#WAP to count number of lines,words,chracters in a given file
import os
fname=input("Enter file name to search : ")
if os.path.isfile("C:/Users/amruth/Desktop/Hemraj/"+fname):
    print("File Exists :",fname)
    f=open("C:/Users/amruth/Desktop/Hemraj/"+fname,'r')
    print(f.read())
    f.seek(0)
    lcount=wcount=ccount=0
    for line in f:
        lcount=lcount+1
        words=line.split()
        wcount=wcount+len(words)
        ccount=ccount+len(line)
    print("Number of lines is :",lcount)
    print("Number of words is :", wcount)
    print("Number of characters is :",ccount)
else:
    print("File doesn't exist")