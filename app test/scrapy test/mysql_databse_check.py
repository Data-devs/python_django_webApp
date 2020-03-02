import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)

if(mysql):
    print('mysql connection : OK')
else:
    print('mysql connection : error')