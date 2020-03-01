#WAP to check whether entered file exist or not

import os
fname=input("Enter file name to search : ")
if os.path.isfile("C:/Users/amruth/Desktop/Hemraj/"+fname):
    print("File exists:", fname)
    f = open("C:/Users/amruth/Desktop/Hemraj/"+fname, 'r')
    print(f.read())
else:
    print("Entered file doesn't exist")
