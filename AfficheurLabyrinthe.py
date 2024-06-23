from tkinter import *

"""
Module qui permet de gÃƒÂ©rer l'affichage d'un labyrinthe sous forme graphique, de maniÃƒÂ¨re simplifiÃƒÂ©e.
Les classes fournies permettent de gÃƒÂ©rer l'affichage de l'ensemble du labyrinthe
et de chaque case (en contrÃƒÂ´lant les murs ÃƒÂ  afficher)
"""

class CaseGraphiqueLabyrinthe:
    """
    Classe permettant de reprÃƒÂ©senter une case sur la grille du labyrinthe
    """
    def __init__(self):
        """
        Constructeur : Initialise une case blanche sans aucun mur actif.
        """
        self.afficher_mur_droit = False
        self.afficher_mur_bas = False
        self.couleur = "#FFFFFF"

    def activer_mur_droit(self):
        """
        Active le mur droit de la case : Il sera dessinÃƒÂ© lors de l'affichage
        """
        self.afficher_mur_droit = True

    def desactiver_mur_droit(self):
        """
        Desactive le mur droit de la case : Il ne sera pas dessinÃƒÂ© lors de l'affichage
        """
        self.afficher_mur_droit = False

    def activer_mur_bas(self):
        """
        Active le mur du bas de la case : Il sera dessinÃƒÂ© lors de l'affichage
        """
        self.afficher_mur_bas = True

    def desactiver_mur_bas(self):
        """
        Desactive le mur du bas de la case : Il ne sera pas dessinÃƒÂ© lors de l'affichage
        """
        self.afficher_mur_bas = False


    def colorier_en_blanc(self):
        """
        RÃƒÂ¨gle la couleur de la case sur blanc
        """
        self.couleur = "#FFFFFF"

    def colorier_en_rouge(self):
        """
        RÃƒÂ¨gle la couleur de la case sur rouge
        """
        self.couleur = "#FF0000"

    def afficherSurLabyrintheGraphique(self, grilleLabyrinthe, i ,j):
        """
        grilleLabyrinthe : Objet LabyryntheGraphique sur lequel case doit ÃƒÂªtre affichÃƒÂ©
        i ,j : CoordonnÃƒÂ©es oÃƒÂ¹ la case doit ÃƒÂªtre affichÃƒÂ©e
        Affiche la case sur la grille grilleLabyrinthe aux coordonnÃƒÂ©es (i,j)
        """
        grilleLabyrinthe.create_rectangle(i*20,j*20,(i+1)*20,(j+1)*20,fill=self.couleur, width=0)
        if self.afficher_mur_droit:
            grilleLabyrinthe.create_rectangle((i+0.8)*20,j*20,(i+1)*20,(j+1)*20,fill="#000000", width=0)
        if self.afficher_mur_bas:
            grilleLabyrinthe.create_rectangle(i*20,(j+0.8)*20,(i+1)*20,(j+1)*20,fill="#000000", width=0)

class LabyryntheGraphique:
    """
    Classe permettant de reprÃƒÂ©senter un Labyrinthe sous forme de grille, dans une fenÃƒÂªtre
    """
    def __init__(self, x, y):
        """
        Constructeur
        x: Largeur du labyrinthe
        y : Hauteur du labyrinthe
        """
        self.x = x
        self.y = y
        self.cases = [[None for i in range(y)] for j in range(x)]

    def ajouterCaseGraphique(self, i, j, case):
        """
        i ,j : CoordonnÃƒÂ©es oÃƒÂ¹ la case doit ÃƒÂªtre stockÃƒÂ©e
        case : Objet CaseGraphiqueLabyrinthe, reprÃƒÂ©sentant la case ÃƒÂ  stocker
        Ajoute la case sur la grille du labyrinthes aux coordonnÃƒÂ©es (i,j)
        """
        self.cases[i][j] = case

    def afficher(self):
        """
        Affiche le labyrinthe dans une nouvelle fenÃƒÂªtre.
        Pour cela, la mÃƒÂ©thode initialise la grille, effectue un parcours
        des objets CaseGraphiqueLabyrinthe stockÃƒÂ©s et les affiche un ÃƒÂ  un (via afficherSurLabyrintheGraphique)
        """
        fenetre=Tk()
        fenetre.state('zoomed')
        fenetre.title("Labyrinthe ("+str(self.x)+ "x" +str(self.y)+")")
        #Initialisation de la grille
        grille=Canvas(fenetre,height=self.y * 20,width=self.x * 20, scrollregion=(0,0,self.x * 20,self.y * 20))
        hbar=Scrollbar(fenetre,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=grille.xview)
        vbar=Scrollbar(fenetre,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=grille.yview)
        grille.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        grille.pack(fill="both", expand=True)
        for i in range(self.x):
            for j in range(self.y):
                case = self.cases[i][j]
                if(case != None):
                    case.afficherSurLabyrintheGraphique(grille, i, j) #Affiche la case sur la grille
        fenetre.mainloop()