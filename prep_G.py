import mysql.connector

def insert_Mammifero():
  nome = input("Inserisci il nome del Mammifero: ")
  peso = float(input("Inserisci il peso del Mammifero: "))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (nome, peso) VALUES (%s, %s)"
val = (Nome, peso)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "mammifero inserito con successo!")

def show_Mammiferis():

  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM Mammiferi")
  # Visualizzazione dei risultati
  for animal in mycursor:
    print(animal)

def delete_animal():
  id = input("Inserisci l'id del mammifero da eliminare: ")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()
sql = "DELETE FROM Mammiferi WHERE id = %s"
val = (id,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "mammifero eliminato con successo!")

def update_animal():
  id = input("Inserisci l'id del mammifero da modificare: ")
  nome = input("Inserisci il nuovo nome del mammifero: ")
  peso = float(input("Inserisci il nuovo peso del mammifero: "))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()
sql = "UPDATE Mammiferi SET nome = %s, peso = %s WHERE id = %s"
val = (nome, peso, id)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "mammifero modificato con successo!")

while True:
  print("Premi 1 per inserire un nuovo animale")
  print("Premi 2 per visualizzare tutti gli animali")
  print("Premi 3 per eliminare un animale")
  print("Premi 4 per modificare un animale")
  print("Premi 5 per uscire dal programma")