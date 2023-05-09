import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zen4321@",
    database="boutique"
)

def get_products():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM produit")
    products = cursor.fetchall()
    return products

def add_product(nom, description, prix, quantite, id_categorie):
    cursor = mydb.cursor()
    sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, description, prix, quantite, id_categorie)
    cursor.execute(sql, val)
    mydb.commit()

def delete_product(id):
    cursor = mydb.cursor()
    sql = "DELETE FROM produit WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()

def update_product(id, quantite, prix):
    cursor = mydb.cursor()
    sql = "UPDATE produit SET quantite = %s, prix = %s WHERE id = %s"
    val = (quantite, prix, id)
    cursor.execute(sql, val)
    mydb.commit()

def show_products():
    products = get_products()
    tk.Label(table_frame, text="ID", padx=5, pady=5).grid(row=0, column=0)
    tk.Label(table_frame, text="Nom", padx=5, pady=5).grid(row=0, column=1)
    tk.Label(table_frame, text="Description", padx=5, pady=5).grid(row=0, column=2)
    tk.Label(table_frame, text="Prix", padx=5, pady=5).grid(row=0, column=3)
    tk.Label(table_frame, text="Quantité", padx=5, pady=5).grid(row=0, column=4)
    tk.Label(table_frame, text="ID catégorie", padx=5, pady=5).grid(row=0, column=5)

    for i, product in enumerate(products):
        for j, value in enumerate(product):
            tk.Label(table_frame, text=value, padx=5, pady=5).grid(row=i, column=j)

def add_product_click():
    nom = nom_entry.get()
    description = description_entry.get()
    prix = prix_entry.get()
    quantite = quantite_entry.get()
    id_categorie = id_categorie_entry.get()
    add_product(nom, description, prix, quantite, id_categorie)
    clear_entries()
    clear_table()
    show_products()

def delete_product_click():
    id = id_entry.get()
    delete_product(id)
    clear_entries()
    clear_table()
    show_products()

def update_product_click():
    id = id_entry.get()
    quantite = quantite_entry.get()
    prix = prix_entry.get()
    update_product(id, quantite, prix)
    clear_entries()
    clear_table()
    show_products()

def clear_entries():
    nom_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    prix_entry.delete(0, tk.END)
    quantite_entry.delete(0, tk.END)
    id_categorie_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)

def clear_table():
    for widget in table_frame.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Gestion de stock")

input_frame = tk.LabelFrame(root, text="Nouveau produit", padx=10, pady=10)
input_frame.grid(row=0, column=0, padx=10, pady=10)

nom_label = tk.Label(input_frame, text="Nom")
nom_label.grid(row=0, column=0)
nom_entry = tk.Entry(input_frame)
nom_entry.grid(row=0, column=1)

description_label = tk.Label(input_frame, text="Description")
description_label.grid(row=1, column=0)
description_entry = tk.Entry(input_frame)
description_entry.grid(row=1, column=1)

prix_label = tk.Label(input_frame, text="Prix")
prix_label.grid(row=2, column=0)
prix_entry = tk.Entry(input_frame)
prix_entry.grid(row=2, column=1)

quantite_label = tk.Label(input_frame, text="Quantité")
quantite_label.grid(row=3, column=0)
quantite_entry = tk.Entry(input_frame)
quantite_entry.grid(row=3, column=1)

id_categorie_label = tk.Label(input_frame, text="ID catégorie")
id_categorie_label.grid(row=4, column=0)
id_categorie_entry = tk.Entry(input_frame)
id_categorie_entry.grid(row=4, column=1)

add_button = tk.Button(input_frame, text="Ajouter", command=add_product_click)
add_button.grid(row=5, column=0, padx=5, pady=5)

delete_button = tk.Button(input_frame, text="Supprimer", command=delete_product_click)
delete_button.grid(row=5, column=1, padx=5, pady=5)

update_button = tk.Button(input_frame, text="Modifier", command=update_product_click)
update_button.grid(row=5, column=2, padx=5, pady=5)

table_frame = tk.LabelFrame(root, text="Liste des produits", padx=10, pady=10)
table_frame.grid(row=1, column=0, padx=10, pady=10)

show_products()

id_label = tk.Label(root, text="ID du produit à supprimer ou modifier")
id_label.grid(row=2, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()