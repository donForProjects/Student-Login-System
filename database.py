import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'xrapidefire05',
    port = '3306',
    database = 'cs_student_info',
    auth_plugin = 'mysq'
)

mycursor = mydb.cursor()


mycursor.execute('SELECT * FROM cs_students')

cs_students = mycursor.fetchall()

for i in cs_students:
    print(i)