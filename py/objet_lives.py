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

class bonus_lives:
    """Création du bonus de vie
    """
    def __init__(self,canvas,width,height):
        self.canvas = canvas 
        self.width_canvas = width
        self.height_canvas = height
        self.give_lives = randint(1,3) # bonus de vie aléatoire en 1 et 3
        self.side = 20 # taille du bonus
        self.x = randint(int(self.side),int(self.width_canvas - self.side)) #coordonnée en x
        self.y = 0 #coordonnée en y
        self.display = None # affichage sur le canvas
        self.velocity = 5 #vitesse 
        self.photo = ImageTk.PhotoImage(Image.open("png/bonus_lives.png").resize((self.side,self.side))) #image du bonus
        
    def display_bonus_lives(self):
        """Affiche le bonus de vie
        """
        self.display = self.canvas.create_image(self.x,self.y,image=self.photo)
    
    def set_coords(self,x,y):
        """Définit les coordonnées du bonus de vie

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y
        """
        self.x = x
        self.y = y
        self.canvas.coords(self.display,x, y)
        
    def move(self):
        """déplace le bonus de vie
        """
        self.y += self.velocity
        self.set_coords(self.x,self.y)
    
        