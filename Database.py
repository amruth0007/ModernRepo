import cx_Oracle
import mymssql
import mypysql


#to establish connection to database
con=cx_Oracle.connect(Database information)

#create cursor object
cursor=con.cursor()

#to execute Queries
cursor.execute(sqlQuery)
cursor.executemany(sqlquery)
cursor.executescript(sqlquery)


#To fetch results
cursor.fetchone()
cursor.fetchall()
cursor.fetchmany(n)


#To pass data
commit()
#to pull back data
rollback()

#To close
cursor.close()
con.close()

#To drop table
drop table  employees

