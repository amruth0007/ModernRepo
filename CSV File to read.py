import csv
f=open("C:/Users/amruth/Desktop/Hemraj/student.csv",'r')
r=csv.reader(f)
data=list(r)
for i in data:
    for j in i:
        print(j,'\t',end='')
    print()
