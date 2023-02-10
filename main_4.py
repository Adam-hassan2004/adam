#mostro i dati nella tabella
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
 #mostro solo un dato dalla tabella

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)