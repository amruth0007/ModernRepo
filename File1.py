#copy from one txt file to another
f1=open('C:/Users/amruth/Desktop/Hemraj/Files.txt','r')
print(f1.tell())
f2=open('C:/Users/amruth/Desktop/Hemraj/output.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print("copied successfully")
