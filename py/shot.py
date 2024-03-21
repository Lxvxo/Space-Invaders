# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 06/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe Shot_alien
Etat du projet : Terminé
"""

# Importations des modules, fonctions ou classes nécessaires

# BEGINNING

class Shot:
    
    def __init__(self,objet : object) -> None:
        self.objet : object = objet 
        self.master = objet.master # fenêtre du jeu
        self.canvas = objet.canvas # Canvas de la partie
        self.attack = objet.attack # dégâts du projectile
        self.velocity = objet.shot_velocity # vitesse du projectile
        self.color = objet.shot_color # couleur du projectile
        self.side = objet.side # taille du lanceur
        self.x = objet.x # coordonnée en x
        self.y = objet.y-objet.side # coordonnée en y
        self.r = 5 # rayon du projectile
        self.display = None # affichage du projectile (canvas_oval)
        self.img = False
        
    def display_shot(self) -> None:
        """Afffiche le projectile sur le Canvas
        """
        if self.objet.exist == False:
            self.display = self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
            self.objet.exist : bool = True
            
    def set_coords(self, x : int, y : int) -> None:
        """Modifie les coordonnée du projectile

        Args:
            x (int): coordonnée en x
            y (int): coordonnée en y
        """
        self.x = x
        self.y = y
        if self.display != None:
            self.canvas.coords(self.display,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)
            
    def move(self) -> None:
        """Déplace le projectile verticalement
        """
        self.y -= self.velocity
        self.set_coords(self.x,self.y)
        
    def attack_objet(self,objet : object) -> None:
        """Attaque l'objet avec le projectile

        Args:
            objet (object): _description_
        """
        objet.lives -= self.attack
        self.canvas.delete(self.display)
        self.display = None
        if objet.lives <=0:
            self.canvas.delete(objet.display)
            objet.display = None
            
class Shot_god(Shot):
    """Définit un tir puissant

    Args:
        Shot (): class Shot
    """
    def __init__(self,objet : object):
        super().__init__(objet)
        self.color = objet.shot_color
        self.r = self.r*2
        self.attack = 100
    def shot_power(self,objet):
        """réaction des éléments qui touchent le tir puissant (ils sont détruits)

        Args:
            objet (object): élément touché
        """
        objet.lives -= self.attack
        if objet.lives <= 0 :
            self.canvas.delete(objet.display)
            objet.display = None
        else : 
            self.canvas.delete(self.display)
            self.display = None
            self.objet.exist : bool = False
            
# END