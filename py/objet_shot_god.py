# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 21/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe bonus
Etat du projet : Terminé 
"""
from PIL import Image,ImageTk
from random import randint

class bonus_shot_god:
    """Création du bonus d'attaque
    """
    def __init__(self,canvas,width,height):
        self.canvas = canvas
        self.width_canvas = width
        self.height_canvas = height
        self.side = 20 #taille du bonus
        self.x = randint(int(self.side),int(self.width_canvas - self.side)) # coordonnée en x
        self.y = 0 # coordonnée en y
        self.number_of_shot = randint(1,3) # nombre de tir puissant aléatoire en 1 et 3
        self.display = None #affichage sur le canvas
        self.velocity = 5 #vitesse du bonus
        self.photo = ImageTk.PhotoImage(Image.open("png/bonus_shot_god.png").resize((self.side,self.side))) # image du bonus
        
    def display_bonus_shot_god(self):
        """Affiche le bonus d'attaque
        """
        self.display = self.canvas.create_image(self.x,self.y,image=self.photo)
    
    def set_coords(self,x,y):
        """Définit les coordonnées du bonus d'attaque

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y
        """
        self.x = x
        self.y = y
        self.canvas.coords(self.display,x, y)
        
    def move(self):
        """déplace le bonus d'attaque
        """
        self.y += self.velocity
        self.set_coords(self.x,self.y)
    
        