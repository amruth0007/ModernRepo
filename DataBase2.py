#WAP to create table and pass value
import cx_Oracle
try:
    query='create table employees(ename varchar(10),esal num(10),eage num(3),eaddr varchar(20))'
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    print("Table created sucessfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem : ",e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
