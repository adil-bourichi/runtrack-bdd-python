import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zen4321@",
    database="LaPlateforme"
)

cursor = db.cursor()

cursor.execute("SELECT SUM(capacite) FROM salles;")

result = cursor.fetchone()[0]

print("La capacités de toutes les salles est de", result)