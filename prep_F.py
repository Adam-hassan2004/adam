import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

val = []
x=int(input("quanti animali vuoi inserire"))
for i in range(x):
    print(f"Inserisci i dati del {i+1}° animale:")

    
    Nome = input("Nome: ")
    Razza = input("Razza: ") 
    eta = int(input("età: "))
    peso = int(input("peso: "))

    val.append( (Nome, Razza, eta, peso) )


print (val)

query = "INSERT INTO Animali (Nome, Specie, Eta) VALUES ( %s, %s,%s,%s)"
cursor.executemany(query, val)
conn.commit()