import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
if con!=None:
    print("Connected successfully")
    print("Version is : ",con.version)
else:
    print("Connection unsuccesfull")
con.close()