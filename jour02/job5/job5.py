#la requete pour sql : [SELECT SUM(superficie) AS total_superficie FROM etage;]

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zen4321@",
    database="LaPlateforme"
)

cursor = db.cursor()

query = "SELECT SUM(superficie) AS total_superficie FROM etage;"
cursor.execute(query)

result = cursor.fetchone()[0]

print("La superficie de La Plateforme est de", result, "m2")

