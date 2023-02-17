import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(255), Razza VARCHAR(255),  età INT(255), peso INT(255))")

