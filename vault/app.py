import customtkinter as ctk
from tkinter import filedialog

from utils import read_file_data

def open_file():
    filepath = filedialog.askopenfilename(title="Chose keyfile")
    if filepath:
        key_input.delete(0, ctk.END)  # Effacer le texte existant dans le champ
        key_input.insert(0, read_file_data(filepath))  # Insérer le chemin du fichier

def unlock_vault():
    print("Unlocking vault with key:", key_input.get())

def create_filekey():
    print("Creating a filekey...")

# Initialiser la fenêtre principale
app = ctk.CTk()
app.geometry("600x400")  # Taille de la fenêtre ajustée
app.title("VaultGuard")

# Champ d'entrée pour la clé
key_input = ctk.CTkEntry(app, width=270, placeholder_text="Key input")
key_input.place(relx=0.62, rely=0.40, anchor="e")  # Centré à gauche

# Bouton "Browse" pour ouvrir un fichier à droite du champ de texte
browse_button = ctk.CTkButton(app, text="Browse", command=open_file)
browse_button.place(relx=0.74, rely=0.40, anchor="center")  # À droite du champ de texte

# Bouton pour déverrouiller le coffre-fort
unlock_button = ctk.CTkButton(app, width=400 , text="Unlock vault", command=unlock_vault)
unlock_button.place(relx=0.5, rely=0.5, anchor="center")  # Centré en dessous

# Bouton pour créer une clé de fichier
create_filekey_button = ctk.CTkButton(app, width=400 , text="Create filekey", command=create_filekey)
create_filekey_button.place(relx=0.5, rely=0.60, anchor="center")  # Centré en dessous

# Lancer l'application
app.mainloop()
