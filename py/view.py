# coding : utf-8
"""
Auteur : SINGARIN-SOLE Livio, PHENG Julien
Date de création : 06/12/2022
Objectif générale : TP-Créer un jeu, le space invaders
Objectif du fichier : Classe View
Etat du projet : Terminé
"""

# Importations des modules, fonctions ou classes nécessaires
from py.game import Game
from tkinter import Button,Frame,Label

from PIL import Image, ImageTk

# BEGINNING
class View :
    """Créer différentes pages pour notre jeu
    """
    def __init__(self,master,width_master : int ,height_master : int ) -> None:
        """Initialisation de la classe View

        Args:
            master (tk): fenêtre du jeu
            width_master (int): longueur de la fenêtre
            height_master (int): hauteur de la fenêtre
        """
        self.master = master
        self.width_master : int = width_master
        self.height_master : int = height_master
        self.state = None # état de la vue
        self.scores_1 = []
        self.scores_2 = []
        self.scores_3 = []
    
    def clear_master(self) -> None : 
        """Nettoie la fenêtre
        """
        
        names_elt : list[str]= []
        for elt in self.master.children:
            names_elt.append(elt)
    
        for elt in names_elt:
            try :
                self.master.children[elt].destroy()
            except : 
                print("destroy échoué")
                
    def home(self, game = None) -> None:
        """Affiche la page d'accueil
        """
        if game != None :
            if game.state == 'end' : 
                if game.level == "1":
                    self.scores_1.append(game.score)
                if game.level == "2":
                    self.scores_2.append(game.score)
                if game.level == "3":
                    self.scores_3.append(game.score)
                    
        self.state : str = "home"
        self.clear_master()
        img = ImageTk.PhotoImage(Image.open("png/home.png").resize((self.width_master+20,self.height_master+20)))

        home_image = Label(self.master,image=img)
        home_image.image = img
        home_image.place(x=-5, y=-5)
        s1 = "Aucun"
        if self.scores_1 != []:
            s1 = self.scores_1.pop()
            self.scores_1.append(s1)
            
        button_play_1 = Button(self.master ,text = "Level 1"  ,font=('Verdana',15,"bold"), 
                            bg = "black", fg ="blue",command = self.game_1 ,
                            pady=15,padx=15,justify="center",highlightthickness=1,bd=1,
                            activebackground="blue",activeforeground="black",overrelief="groove",cursor="circle")
        button_play_1.pack(expand=True,padx = 10,pady=10)
        button_score_1 = Button(self.master ,text = "Dernier Score : " + str(s1)  ,font=('Verdana',10,"bold"), 
                            bg = "black", fg ="blue",command = lambda:self.set_scores(button_score_1,1) ,
                            pady=5,padx=5,justify="center",highlightthickness=1,bd=1,
                            activebackground="blue",activeforeground="black",overrelief="groove",cursor="circle")
        button_play_1.pack(expand=True,padx = 10,pady=10)
        button_score_1.pack(expand=True,padx=5,pady=5)
        
        s2 = "Aucun"
        if self.scores_2 != []:
            s2 = self.scores_2.pop()
            self.scores_2.append(s2)
        button_play_2 = Button(self.master ,text = "Level 2",font=('Verdana',15,"bold"), 
                            bg = "black", fg ="blue",command = self.game_2 ,
                            pady=15,padx=15,justify="center",highlightthickness=1,bd=1,
                            activebackground="blue",activeforeground="black",overrelief="groove",cursor="circle")
        button_score_2 = Button(self.master ,text = "Dernier Score : " + str(s2)  ,font=('Verdana',10,"bold"), 
                            bg = "black", fg ="blue",command = lambda:self.set_scores(button_score_2,2) ,
                            pady=5,padx=5,justify="center",highlightthickness=1,bd=1,
                            activebackground="blue",activeforeground="black",overrelief="groove",cursor="circle")
        button_play_2.pack(expand=True,padx = 10,pady=10)
        button_score_2.pack(expand=True,padx=5,pady=5)
        
        s3 = "Aucun"
        if self.scores_3 != []:
            s3 = self.scores_3.pop()
            self.scores_3.append(s3)
        button_play_3 = Button(self.master ,text = "Level 3",font=('Verdana',15,"bold"), 
                            bg = "black", fg ="blue",command = self.game_3 ,
                            pady=15,padx=15,justify="center",highlightthickness=1,bd=1,
                            activebackground="blue",activeforeground="black",overrelief="groove",cursor="circle")
        button_score_3 = Button(self.master ,text = "Dernier Score : " + str(s3)  ,font=('Verdana',10,"bold"), 
                            bg = "black", fg ="blue",command = lambda:self.set_scores(button_score_3,3) ,
                            pady=5,padx=5,justify="center",highlightthickness=1,bd=1,
                            activebackground="blue",activeforeground="black",overrelief="groove",cursor="circle")
        
        button_play_3.pack(expand=True,padx = 10,pady=10)
        button_score_3.pack(expand=True,padx=5,pady=5)
        button_exit = Button(self.master ,text = "Exit" ,font=('Verdana',15,"bold"), 
                            bg = "black", fg ="magenta",command =self.master.destroy,
                            pady=15,padx=15,justify="center",highlightthickness=1,bd=1,
                            activebackground="magenta",activeforeground="black",overrelief="groove",cursor="circle")
        button_exit.pack(expand=True,padx = 10,pady=10)
        
    def set_scores(self,button_score,level):
        """Affiche le score précédent sur le bouton score

        Args:
            button_score (Button): Bouton qui affiche le dernier score 
            level (int): niveau concerné
        """
        s = "Aucun"
        if level == 1:
            if self.scores_1 != []:
                self.scores_1.pop()
                if self.scores_1 != []:
                    s = self.scores_1.pop()
                    self.scores_1.append(s)
        if level == 2:
            if self.scores_2 != []:
                self.scores_2.pop()
                if self.scores_2 != []:
                    s = self.scores_2.pop()
                    self.scores_2.append(s)
        if level == 3:
            if self.scores_3 != []:
                self.scores_3.pop()
                if self.scores_3 != []:
                    s = self.scores_3.pop()
                    self.scores_3.append(s)
        button_score.config(text = "Dernier Score : " + str(s))
    def game_1(self,game = None) -> None:
        """Crée le niveau 1
        """
        if game != None :
            if game.state == 'end' : 
                if game.level == "1":
                    self.scores_1.append(game.score)
                if game.level == "2":
                    self.scores_2.append(game.score)
                if game.level == "3":
                    self.scores_3.append(game.score)
                    
        self.state : str = "game"
        self.clear_master()
        # création des frames 
        game_frame = Frame(self.master, width =0.75*self.width_master, height = self.height_master, bg = "black")
        menu_frame = Frame(self.master,bg = "#D3D3D3")
        button_frame = Frame(menu_frame,bg="#D3D3D3")

        # initialisation du jeu
        game = Game(self.master,game_frame,self.width_master,self.height_master,"1","png/level_1.png")
        game.display_object()
        self.master.bind("<Key>",game.keyboard)
        
        game.canvas.pack(expand=True)
        
        # création du menu
        
        # création des boutons
        
        # bouton exit
        button_exit = Button(button_frame ,text = "Exit" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command =self.master.destroy ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_exit.pack(side = "left",padx = 5,pady=5)
        # bouton rejouer
        button_replay = Button(button_frame ,text = "Replay" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command = lambda:self.game_1(game) ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_replay.pack(side = "left",padx = 5,pady=5)
        button_home = Button(button_frame ,text = "Home" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command = lambda:self.home(game) ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_home.pack(side = "left",padx = 5,pady=5)
        
        #affichage des frames sous forme de grille 
        game_frame.grid(row = 0, column=0)
        menu_frame.grid(row = 0, column=1)
        
        button_frame.pack(expand=True)

    def game_2(self, game = None) -> None:
        """Crée le niveau 2
        """
        if game != None :
            if game.state == 'end' : 
                if game.level == "1":
                    self.scores_1.append(game.score)
                if game.level == "2":
                    self.scores_2.append(game.score)
                if game.level == "3":
                    self.scores_3.append(game.score)
                    
        self.state : str = "game"
        self.clear_master()
        # création des frames 
        game_frame = Frame(self.master, bg = "black")
        menu_frame = Frame(self.master,bg = "#D3D3D3")
        button_frame = Frame(menu_frame,bg="#D3D3D3")

        # initialisation du jeu
        game = Game(self.master,game_frame,self.width_master,self.height_master,"2","png/level_2.png")
        game.display_object()
        self.master.bind("<Key>",game.keyboard)
        
        game.canvas.pack(expand=True)
        
        # création du menu
        
        # création des boutons
        
        # bouton exit
        button_exit = Button(button_frame ,text = "Exit" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command =self.master.destroy ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_exit.pack(side = "left",padx = 5,pady=5)
        # bouton rejouer
        button_replay = Button(button_frame ,text = "Replay" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command = lambda:self.game_2(game) ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_replay.pack(side = "left",padx = 5,pady=5)
        button_home = Button(button_frame ,text = "Home" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command = lambda:self.home(game) ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_home.pack(side = "left",padx = 5,pady=5)
        
        #affichage des frames sous forme de grille 
        game_frame.grid(row = 0, column=0)
        menu_frame.grid(row = 0, column=1)
        
        button_frame.pack(expand=True)

    def game_3(self, game = None) -> None:
        """Crée le niveau 3
        """
        if game != None :
            if game.state == 'end' : 
                if game.level == "1":
                    self.scores_1.append(game.score)
                if game.level == "2":
                    self.scores_2.append(game.score)
                if game.level == "3":
                    self.scores_3.append(game.score)
                    
        self.state : str = "game"
        self.clear_master()
        # création des frames 
        game_frame = Frame(self.master, bg = "black")
        menu_frame = Frame(self.master,bg = "#D3D3D3")
        button_frame = Frame(menu_frame,bg="#D3D3D3")

        # initialisation du jeu
        game = Game(self.master,game_frame,self.width_master,self.height_master,"3","png/level_3.png")
        game.display_object()
        self.master.bind("<Key>",game.keyboard)

        game.canvas.pack(expand=True)
        
        # création du menu
        
        # création des boutons
        
        # bouton exit
        button_exit = Button(button_frame ,text = "Exit" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command =self.master.destroy ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_exit.pack(side = "left",padx = 5,pady=5)
        # bouton rejouer
        button_replay = Button(button_frame ,text = "Replay" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command = lambda:self.game_3(game) ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_replay.pack(side = "left",padx = 5,pady=5)
        button_home = Button(button_frame ,text = "Home" ,font=('Courier',10,"bold"), 
                            bg = "#D3D3D3", fg ="black",command = lambda:self.home(game) ,
                            pady=5,padx=5,justify="center",highlightthickness=3,bd=3,
                            activebackground="black",activeforeground="#D3D3D3",overrelief="groove",cursor="circle")
        button_home.pack(side = "left",padx = 5,pady=5)
        
        #affichage des frames sous forme de grille 
        game_frame.grid(row = 0, column=0)
        menu_frame.grid(row = 0, column=1)
        
        button_frame.pack(expand=True)

# END
    
    

        
        