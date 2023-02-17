import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (id, Nome, Razza, età, peso) VALUES (%s, %s,%s,%s,%s)"
val = [
  ('1', 'claudia', 'canide', '18', '50'),
  ('2', 'signo', 'cavallide', '18', '70'),
  ('3', 'fed', 'cavallide', '18','65'),
  ('4', 'rebecca','canide','19','60'),
  ('5', 'sium','siummide','33','80')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")