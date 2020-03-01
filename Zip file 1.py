from zipfile import *
f=ZipFile("C:/Users/amruth/Desktop/Hemraj/File7.zip",'w',ZIP_DEFLATED)
f.write('C:/Users/amruth/Desktop/Hemraj/Files.txt')
f.write('C:/Users/amruth/Desktop/Hemraj/output.txt')
f.close()
