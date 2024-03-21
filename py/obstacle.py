# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 13/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe Obstacle
Etat du projet : Terminé
"""
from PIL import Image,ImageTk

class Obstacle:
    """Création d'un obstacle
    """
    def __init__(self, master ,canvas ,width : int , height : int,spaceship) -> None:
        self.master = master
        self.canvas = canvas
        self.width_canvas : int = width
        self.height_canvas : int = height
        self.lives = 20 # point de vie
        self.side = 25 #taille
        self.x = width//2 #coordonnée en x
        self.y = height-2*spaceship.side - 2.5*spaceship.side # corrdonnée en y
        self.display = None #affichage sur le canvas 
        self.color = "white" #couleur du vaisseau si img vaut false
        self.img = True
        self.photo = ImageTk.PhotoImage(Image.open("png/mur.png").resize((self.side,self.side))) #image de l'obstacle
        
    def display_obstacle(self):
        """Affiche l'obstacle sur le canvas
            si img vaut False alors il est représenté par un carré
        """
        if self.img :
            self.display = self.canvas.create_image(self.x,self.y,image=self.photo)
        else:
            self.display = self.canvas.create_rectangle(self.x-self.side,self.y-self.side,self.x+self.side,self.y+self.side,fill=self.color)

    
    def set_coords(self,x : int ,y : int) ->None:
        """Modifie les coordonnées de l'alien

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y
        """
        self.x = x
        self.y = y
        if self.display != None:
            if self.img :
                self.canvas.coords(self.display,x,y)
            else:
                self.canvas.coords(self.display,self.x-self.side,self.y-self.side,self.x+self.side,self.y+self.side)
             
        