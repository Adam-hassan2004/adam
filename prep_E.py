import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Mammiferi WHERE peso > 2")

for animal in mycursor:
  print(animal)