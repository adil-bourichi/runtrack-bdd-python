import mysql.connector

db=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Zen4321@",
    database = "LaPlateforme",
)

mycursor = db.cursor()

mycursor.execute("select*from etudiants")

res = mycursor.fetchall()

for line in res :
    print (line)