import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentationfinal"
)

cursor = db.cursor()
sql="CREATE TABLE clients (Clientid INT AUTO_INCREMENT PRIMARY KEY, Names VARCHAR(255), Surname VARCHAR(255), Price INT (11))"

cursor.execute(sql)