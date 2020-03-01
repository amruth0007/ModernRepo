#WAP to create csv file and to write data
import csv
f=open("C:/Users/amruth/Desktop/Hemraj/student.csv",'w',newline='')
w=csv.writer(f)
w.writerow(['NAME','AGE','MARKS','PERCENTAGE'])
while True:
    name=input("Enter student name :")
    age=int(input("Enter student age :"))
    marks=int(input("Enter student marks :"))
    percentage=int(input("Enter student percentage :"))
    w.writerow([name,age,marks,percentage])
    option=input("Let me know if you still want to continue[Yes|No]:")
    if option.lower()=='no':
        break
print("Data enter sucessfully")
