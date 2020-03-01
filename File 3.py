f=open("C:/Users/amruth/Desktop/Hemraj/bucket2.txt",'r+')
print(f.read())
print("I am at index : ",f.tell()) #25
f.seek(25)
f.write("saturday")  #index will be at last position that is after saturday
f.seek(0)  #so need to move index to 0th position
print(f.read())  # then read from beginning