f1=open("C:/Users/amruth/Desktop/Hemraj/Screeshot/screen.jpg",'rb')
f2=open("C:/Users/amruth/Desktop/Hemraj/Screeshot/screen2.jpg",'wb')
print(f2.write(f1.read()))
print("Copied success")