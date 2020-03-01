import os
from datetime import *
stat1=os.stat('C:/Users/amruth/Desktop/Hemraj/Files.txt')
print("File accessed at :",datetime.fromtimestamp(stat1.st_atime))
print("Last modified at :",datetime.fromtimestamp(stat1.st_mtime))