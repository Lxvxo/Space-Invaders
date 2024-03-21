# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 06/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe Spaceship
Etat du projet : Terminé
"""

# Importations des modules, fonctions ou classes nécessaires
from PIL import Image,ImageTk

# BEGINNING

class Spaceship:
    """Créer un vaisseau
    """
    def __init__(self,master,canvas,width : int , height : int) -> None:
        """Initialisation de la classe Spaceship

        Args:
            master (tk): fenêtre de la partie
            canvas (Canvas): Canvas de la partie
            width (int): longueur du Canvas
            height (int): hauteur du Canvas
        """
        self.master = master
        self.canvas = canvas
        self.width_canvas : int = width
        self.height_canvas : int = height
        self.lives : int = 3 #vie du vaisseau
        self.max_lives : int = 3 #vie maximale du vaisseau
        self.attack : int = 10 # points d'attaque du vaisseau
        self.velocity : int = 15 # vitesse du vaisseau
        self.img : str = True 
        self.side : int = 20 # taille vaisseau
        
        self.photo = ImageTk.PhotoImage(Image.open("png/vaisseau-spatial.png").resize((self.side,self.side))) #image du vaisseau
       
        self.x : int = width/2 # coordonnée en x
        self.y : int = height - 2*self.side  # coordonnée en y
        self.shot : object = None # projectile lancé par le vaisseau
        self.display = None # affichage du vaisseau (canvas_rectagle)
        self.color : str = '#0f056b' # couleur du vaisseau
        #shot
        self.shot_velocity : int = 8 # vitesse du projectile lancé par le vaisseau
        self.shot_color : str = "#8B008B" #couleur du projectile lancé par le vaisseau
        self.exist : bool = False # existence du projectile lancé par le vaisseau
    
    def display_spaceship(self) -> None:
        """Affiche le vaisseau sur le Canvas
            si img vaut False alors il apparaît sous forme de carré sur le canvas
        """
        if self.img :
            self.display = self.canvas.create_image(self.x,self.y,image=self.photo)
        else:
            self.display = self.canvas.create_rectangle(self.x-self.side,self.y-self.side,self.x+self.side,self.y+self.side,fill=self.color)

        
    def move_right(self) -> None:
        """Déplace le vaisseau vers la droite
        """
        self.x += self.velocity
        if self.x >= self.width_canvas-self.side:
            self.x=self.width_canvas-self.side
        self.set_coords(self.x,self.y)
        
    def set_coords(self,x : int ,y : int) -> None:
        """Modifie les coordonnées du spaceship

        Args:
            x (int): coordonnée en x
            y (int): cooordonnée en y
        """
        self.x = x
        self.y = y
        if self.display != None:
            if self.img != None:
                self.canvas.coords(self.display,x,y)
            else:
                self.canvas.coords(self.display,self.x-self.side,self.y-self.side,self.x+self.side,self.y+self.side)
    
    def move_left(self) -> None:
        """Déplace le vaisseau vers la gauche
        """
        self.x -= self.velocity
        if self.x <= self.side:
            self.x = self.side
        self.set_coords(self.x,self.y)
    
    def add_lives(self,live):
        """Ajoute de la vie au vaisseau

        Args:
            live (int): point de vie à rajouter
        """
        self.lives += live
        if self.lives > self.max_lives : 
            self.lives = self.max_lives
        
        
# END
    
        
        
