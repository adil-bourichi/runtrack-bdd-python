import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zen4321@",
    database="LaPlateforme"
)

cursor = db.cursor()
query = "SELECT nom, capacite FROM salles"
cursor.execute(query)
result = cursor.fetchall()

print(result)
