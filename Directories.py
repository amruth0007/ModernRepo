import os

#To get current working directory
cwd=os.getcwd()
print(cwd)

#To create a directory cinemas
os.mkdir('C:/Users/amruth/Desktop/Hemraj/cinemas/hero')
print("Directory created successfully")

#To create multiples directories within a directory
os.makedirs('C:/Users/amruth/Desktop/Hemraj/cinemas/hero/ganesh/friday/week/year')
print("Directory created successfully")

#To remove directory
os.rmdir('C:/Users/amruth/Desktop/Hemraj/cinemas/hero/ganesh/friday/week')
print('Directory removed successfully')

#To rename directories
os.rename('C:/Users/amruth/Desktop/Hemraj/cinemas/hero/ganesh/friday','C:/Users/amruth/Desktop/Hemraj/cinemas/hero/ganesh/Tuesday')
