import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Zen4321@",
  database="entreprise"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS animal (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), race VARCHAR(255), id_cage INT, date_naissance DATE, pays_origine VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS cage (id INT PRIMARY KEY AUTO_INCREMENT, superficie INT, capacite_max INT)")

while True:
    action = input("Voulez-vous ajouter, supprimer ou modifier un animal ou une cage ? (a/s/m/q pour quitter)")
    if action == 'q':
        break
    elif action == 'a':

        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        id_cage = input("ID de la cage : ")
        date_naissance = input("Date de naissance (format : AAAA-MM-JJ) : ")
        pays_origine = input("Pays d'origine de l'animal : ")
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, race, id_cage, date_naissance, pays_origine)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "animal ajouté.")
    elif action == 's':

        id_animal = input("ID de l'animal à supprimer : ")
        sql = "DELETE FROM animal WHERE id = %s"
        val = (id_animal,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "animal supprimé.")
    elif action == 'm':

        id_animal = input("ID de l'animal à modifier : ")
        champ = input("Champ à modifier (nom/race/id_cage/date_naissance/pays_origine) : ")
        nouvelle_valeur = input("Nouvelle valeur : ")
        sql = "UPDATE animal SET " + champ + " = %s WHERE id = %s"
        val = (nouvelle_valeur, id_animal)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "animal modifié.")
    else:
        print("Commande non reconnue.")

mycursor.execute("SELECT * FROM animal")
result = mycursor.fetchall()
for animal in result:
    print(animal)

mycursor.execute("SELECT c.id, a.nom FROM cage c LEFT JOIN animal a ON c.id = a.id_cage")
result = mycursor.fetchall()
for row in result:
    print("Cage", row[0], ":", row[1])



mycursor.execute("SELECT SUM(superficie) FROM cage")
result = mycursor.fetchone()
print("Superficie totale de toutes les cages : ", result[0])
