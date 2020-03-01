#SELECT * from sheet1
#SELECT * from [Orders$B4:Y100]
import adodbapi
import win32com
conn = adodbapi.connect("PROVIDER=Microsoft.ACE.OLEDB.12.0;" 
                        "Data Source = C:\\Users\amruth\Desktop\Hemraj\Read.xlsx;" 
                        "Extended Properties ='Excel 12.0 Xml;HDR=YES'")
cursor = conn.cursor()

cursor.execute("SELECT * FROM [Orders$]")
for row in cursor.fetchall():
    print(row)
# ODBC DRIVER
import pyodbc
conn = pyodbc.connect("DRIVER={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};" 
                      "DBQ=C:\\Users\amruth\Desktop\Hemraj\Read.xlsx;")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sheet1")
for row in cursor.fetchall():
    print(row)