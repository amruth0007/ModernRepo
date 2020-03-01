from zipfile import *
f=ZipFile("C:/Users/amruth/Desktop/Hemraj/File7.zip",'r',ZIP_STORED)
files=f.namelist()
for file in files:
    print("File name is :",file)
    print("Content of file is :")
    f1=open("C:/Users/amruth/Desktop/Hemraj/File7"+file,'r')
    print(f1.read())
    print('*'*10)