# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 21/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : classe Répartition object pour gérer la répartition des aliens et des obstacle
Etat du projet : Terminé
"""

# Importations des modules, fonctions ou classes nécessaires
from py.alien import Alien,Alien_hard,Alien_medium
from py.obstacle import Obstacle
# BEGINNING

class Repartion_object:
    """Création de la class gérant les différentes répartions des éléments sur le canvas
    """
    def __init__(self, master, canvas, width, height, type_repartition,spaceship):
        self.master = master 
        self.canvas = canvas 
        self.width = width
        self.height = height
        self.list_aliens = [] #liste des aliens
        self.list_obstacles = [] # liste des obstacles
        self.type_repartition = type_repartition # type de répartion
        
        if self.type_repartition == "1" :
            self.list_aliens = [Alien(self.master,self.canvas,self.width,self.height) for k in range(30)]
            self.list_obstacles = [Obstacle(self.master,self.canvas,self.width,self.height,spaceship)]
            self.repartition_aliens2(ecart_x=15,ecart_y=30,nb_ligne=3)
            
        if self.type_repartition == "2" :
            self.list_aliens = [Alien_medium(self.master,self.canvas,self.width,self.height) for k in range(20)]+[Alien(self.master,self.canvas,self.width,self.height) for k in range(20)]
            self.list_obstacles = [Obstacle(self.master,self.canvas,self.width,self.height,spaceship) for k in range(5)]
            self.repartition_aliens2(ecart_x=15,ecart_y=30,nb_ligne=4)
            self.repartition_obstacle(ecart = 60)
            
        if self.type_repartition == "3" :
            self.list_aliens = [Alien_hard(self.master,self.canvas,self.width,self.height) for k in range(20)]+[Alien_medium(self.master,self.canvas,self.width,self.height) for k in range(20)] + [Alien(self.master,self.canvas,self.width,self.height) for k in range(20)]
            self.list_obstacles = [Obstacle(self.master,self.canvas,self.width,self.height,spaceship) for k in range(7)]
            self.repartition_aliens2(ecart_x = 10,ecart_y=20,nb_ligne=6)
            self.repartition_obstacle(ecart = 50)
            
    def repartition_aliens(self,ecart = 10) -> None:
        """Répartion des aliens sur une ligne

        Args:
            ecart (int, optional): écart entre deux aliens. Defaults to 5.
        """
        n : int = len(self.list_aliens) - 1
        separation : int = (n // 2) 
        for k in range(separation+1):
            x = self.list_aliens[0].x + (k)*(2*self.list_aliens[k].side + ecart)
            y = self.list_aliens[k].y
            self.list_aliens[k].set_coords(x,y)
        for k in range(separation+1,n+1):
            x = self.list_aliens[0].x - (k-separation)*(2*self.list_aliens[k].side + ecart)
            y = self.list_aliens[k].y
            self.list_aliens[k].set_coords(x,y)
            
    def repartition_aliens2(self,ecart_x=10,ecart_y=20,nb_ligne=6):
        """Répartion des aliens sur plusieurs lignes

        Args:
            ecart_x (int, optional): écart en x. Defaults to 10.
            ecart_y (int, optional): écart en y. Defaults to 20.
            nb_ligne (int, optional): nombre de lignes. Defaults to 6.
        """
        nb_aliens_ligne = len(self.list_aliens)//nb_ligne
        lignes = [nb_aliens_ligne for k in range(nb_ligne-1)]
        lignes.insert(0,nb_aliens_ligne+len(self.list_aliens)%nb_ligne)
        for i in range(nb_ligne):
            n : int = lignes[i] - 1
            separation : int = (n // 2) 
            for k in range(separation+1):
                x = self.list_aliens[lignes[i]*i].x + (k)*(2*self.list_aliens[k+lignes[i]*i].side + ecart_x)
                y = self.list_aliens[k+lignes[i]*i].y + (i)*(2*self.list_aliens[k+lignes[i]*i].side + ecart_y)
                self.list_aliens[k+lignes[i]*i].set_coords(x,y)
            for k in range(separation+1,n+1):
                x = self.list_aliens[lignes[i]*i].x - (k-separation)*(2*self.list_aliens[k+lignes[i]*i].side + ecart_x)
                y = self.list_aliens[k+lignes[i]*i].y + (i)*(2*self.list_aliens[k+lignes[i]*i].side + ecart_y)
                self.list_aliens[k+lignes[i]*i].set_coords(x,y)
            
        
    def repartition_obstacle(self,ecart=50):
        """Répartion des obstacles sur une ligne

        Args:
            ecart (int, optional): écart. Defaults to 50.
        """
        n : int = len(self.list_obstacles) - 1
        separation : int = (n // 2) 
        for k in range(separation+1):
            x = self.list_obstacles[0].x + (k)*(2*self.list_obstacles[k].side + ecart)
            y = self.list_obstacles[k].y
            self.list_obstacles[k].set_coords(x,y)
        for k in range(separation+1,n+1):
            x = self.list_obstacles[0].x - (k-separation)*(2*self.list_obstacles[k].side + ecart)
            y = self.list_obstacles[k].y
            self.list_obstacles[k].set_coords(x,y)










# END