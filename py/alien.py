# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création: 06/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe Alien
Etat du projet : Terminé
"""

# Importations des modules, fonctions ou classes nécessaires
from PIL import Image,ImageTk

# BEGINNING

class Alien:
    """Créer un alien
    """
    def __init__(self,master,canvas,width : int ,height : int) -> None:
        """Initialisation de la classe Alien

        Args:
            master (tk): fenêtre de la partie
            canvas (Canvas): Canvas de la partie
            width (int): longueur du Canvas
            height (int): hauteur du canvas
        """
        self.master = master
        self.canvas = canvas
        self.width_canvas  : int = width
        self.height_canvas : int = height
        self.lives : int = 10 # vie de l'alien
        self.attack  : int = 1 # point d'attaque de l'alien
        self.velocity : int = 20 # vitesse de l'alien
        self.img : str = None # image de l'alien
        self.side : int = 20 # taille de l'alien 
        self.x : int = self.width_canvas/2 # coordonnée en x 
        self.y : int = 5*self.side # coordonnée en y
        self.img : str = True 
        self.photo = ImageTk.PhotoImage(Image.open("png/alien_1.png").resize((self.side,self.side))) #image de l'alien
        self.shot : object = None # projectile lancé par l'alien
        self.display = None # #affichage de l'alien (canvas_rectagle)
        self.color : str = '#32CD32' # couleur de l'alien
        #shot
        self.shot_velocity : int= -8 # vitesse du projectile lancé l'alien (négatif car l'alien tire vers le bas)
        self.shot_color : str = "#32CD32" # couleur du projectile lancé par l'alien
        self.exist : bool = False # existence du projectile lancé par le vaisseau
        self.score = 10 # score octroyé
        
    def display_alien(self) -> None:
        """Affiche l'alien sur le canvas 
            si img vaut False alors il apparaît sous forme de carré sur le canvas
        """
        if self.img :
            self.display = self.canvas.create_image(self.x,self.y,image=self.photo)
        else :
            self.display = self.canvas.create_rectangle(self.x-self.side,0,self.x+self.side,self.y+self.side,fill=self.color)

    def set_coords(self,x : int ,y : int) ->None:
        """Modifie les coordonnées de l'alien

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y
        """
        self.x = x
        self.y = y
        if self.display != None:
            if self.img:
                self.canvas.coords(self.display,x,y)
            else :
                self.canvas.coords(self.display,self.x-self.side,self.y-self.side,self.x+self.side,self.y+self.side)
             
    def move(self) -> None:
        """Déplace l'alien horizontalement
        """
        self.x+=self.velocity
        
        
    def touch_spaceship(self,objet : object):
        """Définit le comportement de l'alien lorsqu'il touche le vaisseau

        Args:
            objet (object): spaceship
        """
        self.canvas.delete(self.display)
        self.display = None
        objet.lives-=1 # lorsque que l'alien touche le vaisseau il lui retire 1 point de vie
        if objet.lives == 0: 
            self.canvas.delete(objet.display)
            objet.display = None
          
    def touch_obstacle(self,objet : object):
        """Définit le comportement de l'alien lorsqu'il touche un obstacle

        Args:
            objet (object): obstacle
        """
        self.canvas.delete(self.display)
        self.display=None
        objet.lives-= self.attack*2 # # lorsque que l'alien touche l'obstacle il lui retire 2 x ses points d'attaque
        if objet.lives == 0:
            self.canvas.delete(objet.display)
            objet.display = None

class Alien_medium(Alien):
    """définit une autre classe d'alien de puissance moyenne

    Args:
        Alien (): class Alien
    """
    def __init__(self,master,canvas,width : int ,height : int):
        super().__init__(master,canvas,width,height)
        self.color : str = 'magenta'
        self.attack  : int = 1
        self.lives = 20
        self.shot_color : str = "magenta" # couleur du projectile lancé par l'alien
        self.score = 20
        self.photo = ImageTk.PhotoImage(Image.open("png/alien_2.png").resize((self.side,self.side)))
        

class Alien_hard(Alien):
    """définit une autre classe d'alien de puissance élevée

    Args:
        Alien (): class Alien
    """
    def __init__(self,master,canvas,width : int ,height : int):
        super().__init__(master,canvas,width,height)
        self.color : str = 'red'
        self.attack  : int = 1
        self.lives = 30
        self.shot_color : str = "red" # couleur du projectile lancé par l'alien
        self.score = 30
        self.photo = ImageTk.PhotoImage(Image.open("png/alien_3.png").resize((self.side,self.side)))


class Boss(Alien):
    """définit une autre classe d'alien pour le boss normale

    Args:
        Alien (): class Alien
    """
    def __init__(self,master,canvas,width : int ,height : int):
        super().__init__(master,canvas,width,height)
        self.velocity = 8
        self.color : str = 'black'
        self.attack  : int = 1
        self.y = self.height_canvas//2
        self.side = self.side*8
        self.lives = 200
        self.shot_color : str = "black" # couleur du projectile lancé par l'alien
        self.score = 500
        self.photo = ImageTk.PhotoImage(Image.open("gif/boss_1.gif").resize((self.side,self.side)))

class Boss_medium(Boss):
    """définit une autre classe d'alien pour le boss moyen

    Args:
        Boss (): class Boss
    """
    def __init__(self,master,canvas,width : int ,height : int):
        super().__init__(master,canvas,width,height)
        self.attack  : int = 2
        self.lives = 500
        self.score = 1000
        self.photo = ImageTk.PhotoImage(Image.open("gif/boss_2.gif").resize((self.side,self.side)))

class Boss_hard(Boss):
    """définit une autre classe d'alien pour le boss hard

    Args:
        Boss (): class Boss
    """
    def __init__(self,master,canvas,width : int ,height : int):
        super().__init__(master,canvas,width,height)
        self.attack  : int = 2
        self.lives = 1000
        self.score = 10000
        self.photo = ImageTk.PhotoImage(Image.open("gif/boss_3.gif").resize((self.side,self.side)))



# END