import mysql.connector

MyDB = mysql.connector.connect(host='localhost', user='Banu', passwd='Banu@5', database='learning')

MyCursor = MyDB.cursor()
MyCursor.execute("select * from student")
Data = MyCursor.fetchall()
for i in Data:
    print(i)

