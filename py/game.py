# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 06/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe Game
Etat du projet : Terminé 
"""

# Importations des modules, fonctions ou classes nécessaires
from py.spaceship import Spaceship
from py.shot import Shot,Shot_god
from tkinter import Canvas
import random 
from py.repartion_object import Repartion_object
from tkinter import Canvas
from PIL import Image, ImageTk
from py.ufo import UFO
from py.objet_lives import bonus_lives
from py.objet_shot_god import bonus_shot_god
from py.alien import Boss,Boss_medium,Boss_hard
# BEGINNING

class Game:
    """Caractéristiques du jeu
    """
    def __init__(self,master,frame,width_master : int, height_master : int, level : str, path_img : str) -> None:
        """Initialisation de la classe Game

        Args:
            master (tk): fenêtre
            frame (Frame): frame de la partie
            width_master (int): longueur de la fenêtre
            height_master (int): hauteur de la fenêtre
        """
        self.master = master
        self.width : int = 0.75*width_master
        self.height : int = height_master
        self.frame = frame
        self.canvas = Canvas(self.frame,width = self.width, height = self.height,bg = "black")
        self.level = level
        self.spaceship = Spaceship(self.master,self.canvas,self.width,self.height)
        self.score : int = 0 # score
        self.repartion_object = Repartion_object(self.master,self.canvas,self.width,self.height,self.level,self.spaceship) # la répartition des aliens et des obstacles dans le canvas

        self.aliens : list[object] = self.repartion_object.list_aliens # liste des aliens
        
        self.img : str = ImageTk.PhotoImage(Image.open(path_img).resize((int(self.width)+1,int(self.height)+1))) #image du premier niveau
        self.img_lose : str = ImageTk.PhotoImage(Image.open("png/lose.png").resize((int(self.width)+1,int(self.height)+1)))
        self.img_won : str = ImageTk.PhotoImage(Image.open("png/won.png").resize((int(self.width)+1,int(self.height)+1)))
        self.nb_aliens = len(self.aliens)
        self.state : str = "current" #état du jeu
        self.score_label = self.canvas.create_text(50,10,text="Score : " + str(self.score),fill="white", font="Courier 10") # affichage du score
        self.lives_label = self.canvas.create_text(self.width -80,10,text="Lives : " + str(self.spaceship.lives),fill="white", font="Courier 10") # affichage des points des vies
        self.obstacle = self.repartion_object.list_obstacles
        self.god = 0 # stocke le nombre de coups puissant que peut lancer le vaisseau
        self.ufo = None # la soucoupe 
        self.bonus_lives = None # le bonus de vie quand il apparaît
        self.bonus_shot_god = None #le bonus d'attaque puissante lorsqu'il apparaît
        if self.level == "1" :
            self.boss = Boss(self.master,self.canvas,self.width,self.height)
        if self.level == "2" :
            self.boss = Boss_medium(self.master,self.canvas,self.width,self.height)
        if self.level == "3" :
            self.boss = Boss_hard(self.master,self.canvas,self.width,self.height)
        self.exist_boss = False
        
        
    def display_object(self) -> None:
        """affiche et met en mouvement les objets de la partie 
        """
        self.canvas.create_image(self.width/2,self.height/2,image=self.img)
        self.spaceship.display_spaceship()
        for alien in self.aliens : 
            alien.display_alien()
        for obstacl in self.obstacle:
            obstacl.display_obstacle()
        self.deplacement_aliens()
        for k in range(len(self.aliens)//4):
            self.shot_random()
        self.alien_touch()
        self.all_ufo()
        self.display_bonus()
        
        
    def end_game(self) -> None:
        """Affiche l'écran de fin de partie
        """
        if self.spaceship.lives <= 0:
            texte = "GAME OVER !"
        if len(self.aliens) == 0 and self.boss.lives <= 0 and self.spaceship.display != None:
            texte = "YOU WON !"
        else:
            texte = "GAME OVER !"
        self.state = "end"
        self.canvas.delete("all")
        if texte == "GAME OVER !" : 
            self.canvas.create_image(self.width/2,self.height/2,image=self.img_lose)
        else:
            self.canvas.create_image(self.width/2,self.height/2,image=self.img_won)
        self.canvas.create_text(self.width/2,self.height/2,text =texte,font="Algerian 50",fill = "white")
        self.score_label = self.canvas.create_text(self.width/2,self.height/2 + 50,text="Score : " + str(self.score),fill="white", font="Courier 30")
    
    def set_label_score(self,score)->None :
        """Modifie et affiche le score de la partie
        """
        self.set_aliens()
        self.score += score
        self.canvas.delete(self.score_label)
        self.score_label = self.canvas.create_text(50,10,text="Score : " + str(self.score),fill="white", font="Courier 10")
        
    def set_label_lives(self)->None :
        """Modifie et affiche les points de vie du vaisseau
        """
        self.canvas.delete(self.lives_label)
        self.lives_label = self.canvas.create_text(self.width -70,10,text="Lives : " + str(self.spaceship.lives),fill="white", font="Courier 10")
    
    def keyboard(self,event) -> None:
        """Gère les touches du clavier

        Args:
            event (event): évènement : appuyer sur une touche
        """
        if self.spaceship.display != None :
            if event.keysym =="Right":
                self.spaceship.move_right()
            if event.keysym == "Left":
                self.spaceship.move_left()
            if event.keysym == "space" and self.spaceship.exist== False:
                if self.god != 0 :
                    self.shot_spaceship_god()
                    self.god -=1
                else:
                    self.shot_spaceship()
            if event.keysym == "v": #en appuyant v on peut se rajouter de la vie
                self.spaceship.lives +=10
                self.set_label_lives()
            # if event.keysym == "b": #en appuyant b on peut lancer des tirs puissants en illimité
            #     self.shot_spaceship_god()
                
                
    def set_aliens(self) -> None:
        """Met a jour la liste des aliens
        """
        v : int = -1
        while v != 0:
            v : int =0
            for k in range(len(self.aliens)):
                if self.aliens[k].display == None :
                    v+=1
                    del self.aliens[k]
                    break
                    
    def set_obstacle(self) -> None:
        """Met a jour la liste des obstacles
        """
        v : int = -1
        while v != 0:
            v : int =0
            for k in range(len(self.obstacle)):
                if self.obstacle[k].display == None :
                    v+=1
                    del self.obstacle[k]
                    break
                
    def deplacement_aliens(self) -> None:
        """Déplace les aliens 
        """
        self.set_aliens()
        v : int = 0 # variable pour savoir si un des aliens touche la bordure
        for alien in self.aliens :
             
                if len(self.aliens) <= self.nb_aliens//4:
                    alien.move()
                alien.move()   
                if alien.x>= self.width-alien.side:
                    v+=1
                if alien.x <= alien.side:
                    v+=1
                if alien.y > self.height-alien.side:
                    for alien in self.aliens:
                        alien.display = None
                    self.spaceship.display = None
                    self.set_aliens()
                    self.end_game()
                    
        if v>0 :
             for alien in self.aliens : 
                    alien.x -= alien.velocity
                    alien.velocity = -alien.velocity
                    alien.y += 2*alien.side
        self.set_aliens()            
        for alien in self.aliens :
            alien.set_coords(alien.x,alien.y)
            
        
        self.master.after(1200,self.deplacement_aliens)
        
    def alien_touch(self) -> None:
        """Réaction de l'alien s'il touche le vaisseau ou un obstacle
        """
        if self.spaceship.display != None:
            if self.spaceship.img :
                xmin,ymin,xmax,ymax = self.spaceship.x - self.spaceship.side, self.spaceship.y-self.spaceship.side, self.spaceship.x + self.spaceship.side, self.spaceship.y+self.spaceship.side
            else :
                xmin,ymin,xmax,ymax = self.canvas.coords(self.spaceship.display)
            for alien in self.aliens:
                if xmin <= alien.x<=xmax and ymin<=alien.y<= ymax:
                    alien.touch_spaceship(self.spaceship)
                    self.set_label_lives()
                    if self.spaceship.lives == 0:
                        self.set_aliens()
                        self.end_game()
        self.set_obstacle()
        if len(self.obstacle) != 0:
            for obstacle in self.obstacle:
                if obstacle.img :
                    xmin,ymin,xmax,ymax = obstacle.x - obstacle.side, obstacle.y-obstacle.side, obstacle.x + obstacle.side, obstacle.y+obstacle.side
                else :
                    xmin,ymin,xmax,ymax = self.canvas.coords(obstacle.display)
                for alien in self.aliens:
                    if xmin <= alien.x<=xmax and ymin<=alien.y<= ymax:
                        alien.touch_obstacle(obstacle)
        if len(self.aliens) == 0:
            self.display_boss()
        self.master.after(30,self.alien_touch)
                    
    def shot_(self, objet : object) -> None:
        """Lance un projectile

        Args:
            objet (object): objet qui lance le projectile
        """
        if objet.exist == False : 
            objet.shot : object = Shot(objet)
            objet.shot.display_shot()
    def shot_god(self, objet : object) -> None:
        """Lance un projectile puissant

        Args:
            objet (object): objet qui lance le projectile
        """
        if objet.exist == False : 
            objet.shot : object = Shot_god(objet)
            objet.shot.display_shot()
            
    def deplacement_shot(self,objet : object , ennemis : list[object] ) -> None:
        """Déplace le projectile et élimine l'ennemi si touché

        Args:
            objet (object): objet qui lance le projectile
            ennemis (list[object]): ennemis
        """
        self.set_aliens()
        if objet.exist:
            for elt in ennemis:
                if elt.display != None:
                    if elt.img :
                        xmin,ymin,xmax,ymax = elt.x - elt.side, elt.y - elt.side, elt.x + elt.side, elt.y + elt.side
                    else :
                        
                        xmin,ymin,xmax,ymax = self.canvas.coords(elt.display)
                
                    if xmin<=objet.shot.x<=xmax and ymin<=objet.shot.y<= ymax:
                        objet.shot.attack_objet(elt)
                        objet.exist : bool = False
                        if objet == self.spaceship:
                            if elt.lives <= 0 :
                                self.set_label_score(elt.score)
                        self.set_label_lives()
                        break

            if self.spaceship.lives <= 0 : 
                self.end_game()
            if len(self.aliens) == 0:
                self.display_boss()
                if self.boss.lives <= 0 :
                    self.end_game()
                
        if objet.exist: 
            if objet.shot.y <= objet.shot.r:
                self.canvas.delete(objet.shot.display)
                objet.shot.display = None
                objet.exist : bool = False
        if objet.exist: 
            if objet.shot.y >= self.height - objet.shot.r:
                self.canvas.delete(objet.shot.display)
                objet.shot.display = None
                objet.exist : bool = False
        
        if objet.exist: 
            objet.shot.move()
            self.master.after(30,lambda:self.deplacement_shot(objet,ennemis))

    def shot_spaceship(self) -> None:
        """Le vaisseau lance un projectile
        """
        self.set_aliens()
        self.shot_(self.spaceship)
        self.deplacement_shot(self.spaceship, self.aliens+[self.ufo])
        if self.exist_boss == True:
            self.deplacement_shot(self.spaceship, [self.boss]+[self.ufo])
    def deplacement_shot_god(self,objet : object , ennemis : list[object] ) -> None:
        """Déplace le projectile puissant et élimine l'ennemi si touché

        Args:
            objet (object): objet qui lance le projectile
            ennemis (list[object]): ennemis
        """
        self.set_aliens()
        if objet.exist:
            for elt in ennemis:
                if elt.display != None:
                    if elt.img:
                        xmin,ymin,xmax,ymax = elt.x - elt.side, elt.y - elt.side, elt.x + elt.side, elt.y + elt.side
                    else:
                        xmin,ymin,xmax,ymax = self.canvas.coords(elt.display)
                
                    if xmin<=objet.shot.x<=xmax and ymin<=objet.shot.y<= ymax:
                        objet.shot.shot_power(elt)
                        self.set_label_score(elt.score)
            
            if self.spaceship.lives <= 0 : 
                self.end_game()
                
            if len(self.aliens) == 0:
                self.display_boss()
                if self.boss.lives <= 0 :
                    self.end_game()
                  
        if objet.exist: 
            if objet.shot.y <= objet.shot.r:
                self.canvas.delete(objet.shot.display)
                objet.shot.display = None
                objet.exist : bool = False
        if objet.exist: 
            if objet.shot.y >= self.height - objet.shot.r:
                self.canvas.delete(objet.shot.display)
                objet.shot.display = None
                objet.exist : bool = False
        
        if objet.exist: 
            objet.shot.move()
            self.master.after(30,lambda:self.deplacement_shot_god(objet,ennemis))
        
    def shot_spaceship_god(self):
        """envoie un tir puissant qui détruit tout les ennemis sur son passage
        """
        self.set_aliens()
        self.shot_god(self.spaceship)
        self.deplacement_shot_god(self.spaceship,self.aliens+[self.ufo])
        if self.exist_boss == True:
            self.deplacement_shot(self.spaceship,self.obstacle+ [self.boss]+[self.ufo])
    
        
    def shot_alien(self) -> None :
        """Un alien choisi aléatoirement lance un projectile
        """
        self.set_aliens()
        self.set_obstacle()
        
        indice_alien_random = random.randint(0,len(self.aliens)-1)
        if self.aliens[indice_alien_random].exist :
            pass
        else :
            self.shot_(self.aliens[indice_alien_random])
            self.deplacement_shot(self.aliens[indice_alien_random],[self.spaceship]+self.obstacle)
        
    def shot_random(self) -> None :
        """répète shot_alien jusqu'à la fin du fin
        """
        if self.state != "end":
            self.shot_alien()
            self.master.after(3000,self.shot_random)
    
    def new_ufo(self):
        """Génère la soucoupe volante et la met en mouvement
        """
        self.ufo = UFO(self.canvas,self.width,self.height)
        self.ufo.display_ufo()
        self.deplacement_ufo()
        
    def deplacement_ufo(self):
        """Met en mouvement la soucoupe volante
        """
        if self.ufo.display != None:
            self.ufo.move()
            if self.ufo.x >= self.width + self.ufo.side:
                self.canvas.delete(self.ufo.display)
                self.ufo.display = None
            self.master.after(50,self.deplacement_ufo)
        
    def all_ufo(self):
        """Génère des soucoupe volantes à intervalle de temps régulier
        """
        self.new_ufo()
        self.master.after(35000,self.all_ufo)
        
    def new_bonus_lives(self):
        """Génère un bonus de vie
        """
        self.bonus_lives = bonus_lives(self.canvas,self.width,self.height)
        self.bonus_lives.display_bonus_lives()
        self.deplacement_bonus_lives()
        
    def deplacement_bonus_lives(self):
        """met en mouvement verticalement le bonus de vie
        """
        if self.bonus_lives.display != None:
            self.bonus_lives.move()
            if self.bonus_lives.y >= self.height + self.bonus_lives.side:
                self.canvas.delete(self.bonus_lives.display)
                self.bonus_lives = None
            self.master.after(30,self.deplacement_bonus_lives)
    
    def new_bonus_shot_god(self):
        """génère un bonus d'attaque puissante
        """
        self.bonus_shot_god = bonus_shot_god(self.canvas,self.width,self.height)
        self.bonus_shot_god.display_bonus_shot_god()
        self.deplacement_bonus_shot_god()
        
    def deplacement_bonus_shot_god(self):
        """met en mouvement un bonus d'attaque puissante
        """
        if self.bonus_shot_god.display != None:
            self.bonus_shot_god.move()
            if self.bonus_shot_god.y >= self.height + self.bonus_shot_god.side:
                self.canvas.delete(self.bonus_shot_god.display)
                self.bonus_shot_god = None
            self.master.after(30,self.deplacement_bonus_shot_god)
    
    
    def new_bonus(self):
        """Choisit un bonus aléatoire
        """
        i = random.randint(0,1)
        if i == 0 :
            self.new_bonus_shot_god()
        if i == 1 :
            self.new_bonus_lives()
        self.master.after(30000,self.new_bonus)
    
    def touch_bonus(self):
        """Réaction du vaisseau lorsqu'il touche l'un des deux bonus
        """
        if self.spaceship.img :
                
            xmin,ymin,xmax,ymax = self.spaceship.x - self.spaceship.side, self.spaceship.y-self.spaceship.side, self.spaceship.x + self.spaceship.side, self.spaceship.y+self.spaceship.side
        
        else :
            
            xmin,ymin,xmax,ymax = self.canvas.coords(self.spaceship.display)
                
        if self.bonus_lives != None : 
            if xmin<= self.bonus_lives.x <= xmax and ymin <= self.bonus_lives.y <= ymax:
                self.spaceship.add_lives(self.bonus_lives.give_lives)
                self.set_label_lives()
                self.canvas.delete(self.bonus_lives.display)
                self.bonus_lives = None
        if self.bonus_shot_god != None :
            
            if xmin<= self.bonus_shot_god.x <= xmax and ymin <= self.bonus_shot_god.y <= ymax:
                self.god += self.bonus_shot_god.number_of_shot
                self.canvas.delete(self.bonus_shot_god.display)
                self.bonus_shot_god = None
        self.master.after(30,self.touch_bonus)
        
    def display_bonus(self):
        """Génère des bonus aléatoire à intervalle de temps régulier
        """
        self.new_bonus()
        self.touch_bonus()
    
    def display_boss(self):
        """affiche les boss
        """
        if self.exist_boss == False :
            self.boss.display_alien()
            self.exist_boss = True
            self.deplacement_boss()
            self.shot_boss()
            
    def deplacement_boss(self):
        """Gère le déplacement du boss
        """
        self.boss.move()
        if self.boss.x>= self.width-self.boss.side:
            self.boss.x = self.width-self.boss.side
            self.boss.velocity = -self.boss.velocity
        if self.boss.x <= self.boss.side:
            self.boss.velocity = -self.boss.velocity
            self.boss.x = self.boss.side
        self.boss.set_coords(self.boss.x,self.boss.y)
        if self.boss.lives == 0 :
            self.boss = None
            self.end_game()
        if self.spaceship.lives == 0:
            self.end_game()
        self.master.after(30,self.deplacement_boss)
        
    def shot_boss(self):
        """Gère les tirs du boss
        """
        self.set_obstacle()
        nb = random.randint(1,3)
        if nb == 3 :
            self.shot_god(self.boss)
            self.deplacement_shot_god(self.boss,[self.spaceship]+self.obstacle)
        else:
            self.shot_(self.boss)
            self.deplacement_shot(self.boss,[self.spaceship]+self.obstacle)
        self.master.after(1000,self.shot_boss)

# END
        
    