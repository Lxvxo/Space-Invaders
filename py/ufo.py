# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 21/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe UFO
Etat du projet : Terminé
"""
# Importations des modules, fonctions ou classes nécessaires
from PIL import Image,ImageTk

class UFO:
    """Défint une soucoupe volante qui rajoute du score
    """
    def __init__(self,canvas,width,height):
        self.canvas = canvas
        self.width_canvas = width
        self.height_canvas = height
        self.lives = 1 # point de vie
        self.attack = 0 #point d'attaque
        self.side = 25 #taille de la soucoupe
        self.photo = ImageTk.PhotoImage(Image.open("png/ufo.png").resize((self.side,self.side))) #image de la soucoupe
        self.img = True
        self.color = "white" # couleur si img vaut false
        self.x = 0 #coordonnée en x
        self.y = 1.5*self.side #coordonnée en y
        self.score = 50 # score octroyé
        self.velocity = 3 #vitesse de la soucoupe
        self.display = None #affichage sur le canvas
    
    def display_ufo(self):
        """Affiche la soucoupe volante sur le canvas
            si img vaut false, celle ci est représenté sous forme de carré
        """
        if self.img :
            self.display = self.canvas.create_image(self.x,self.y,image=self.photo)
        else:
            self.display = self.canvas.create_rectangle(self.x-self.side,self.y-self.side,self.x+self.side,self.y+self.side,fill=self.color)

    def move(self):
        """Déplace la soucoupe volante
        """
        self.x += self.velocity
        self.set_coords(self.x,self.y)
        
    def set_coords(self,x,y):
        """définit les coordonnées de la soucoupe

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y
        """
        self.x = x
        self.y = y 
        self.canvas.coords(self.display,x,y)