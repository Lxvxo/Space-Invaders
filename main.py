# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date : 06/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Fichier principale pour lancer le jeu
Etat du projet : Terminé
"""

# Importations des modules, fonctions ou classes nécessaires
from tkinter import Tk
from py.view import View

# BEGINNING

# création de la fenêtre
window = Tk()
window.title("Space invaders")
width = 1200
height = 700
window.geometry("{}x{}".format(width,height)) 
window.iconbitmap("ico\icone.ico")
window.config(background="#D3D3D3") # ~ gris

# création de la vue
View_ = View(window,width,height)
View_.home()

# activation du déroulement des évènements
window.mainloop()

# END