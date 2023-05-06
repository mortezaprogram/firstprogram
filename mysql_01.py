
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='192.168.135.129',database='students', user='studentadmin',password='P@ssw0rd')
    query = 'SELECT sex, COUNT(*)  FROM student GROUP BY sex'
    #query = 'SELECT CONCAT(first_name, " ", last_name) AS "Name", CONCAT(city, ", ", state) AS "Hometown"  FROM students'
    cursor=conn.cursor()
    cursor.execute(query)
    student=cursor.fetchall()
    print("Total Results: ",len(student))
    for s in student:
        print(s[0]," ",s[1])
except mysql.connector.Error as error:
        print("Error :", error)
finally:
    if (conn.is_connected()):
         conn.close()