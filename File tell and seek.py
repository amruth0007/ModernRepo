#Tell method will tell where exactly the cursor is
#seek method ,using this we can move the cursor to which ever index we want starting from 0th index
f=open('C:/Users/amruth/Desktop/Hemraj/Patterns.txt','r')
print("I am at index : ",f.tell())
print(f.read(10))

print("I am at index : ",f.tell())
print(f.read(15))

print("I am at index : ",f.tell())
print(f.read(3))

f.seek(0)
print(f.read(5))
print("I am at index : ",f.tell())


