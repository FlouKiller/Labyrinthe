from Noeud import NoeudBinaire
from random import randint
from afficheur_arbre import afficher_arbre
from AfficheurLabyrinthe import *
from File import File


"""
Classe permettant de gÃ©nÃ©rer un labyrinthe sous la forme d'un arbre binaire.
On peut Ã©galement afficher et rÃ©soudre la labyrinthe.
"""
class Labyrinthe:
    def __init__(self, x, y):
        """
        Constructeur
        x: Largeur du labyrinthe
        y : Hauteur du labyrinthe
        """
        self.x = x
        self.y = y
        self.genererLabyrinthe()

    def genererLabyrinthe(self):
        """
        GÃ©nÃ©Ã¨re le labyrinthe en crÃ©ant les relations entre les noeuds suivant la mÃ©thode de gÃ©nÃ©ration avec un abre binaire.
        A la fin, self.entree contient la racine de l'arbre.
        Ne retourne rien
        """

        cases = [[NoeudBinaire((i,j), None, None) for j in range(self.y)] for i in range (self.x)]
        for i in range(len(cases)):
            for j in range(len(cases[i])):
                case_a_ouvrir = randint(0, 1)
                case_actuelle = cases[i][j]
                #0 = en haut 1 = à gauche
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    case_a_ouvrir = 0
                if j == 0:
                    case_a_ouvrir = 1

                if case_a_ouvrir == 0:
                    cases[i][j-1].fils_gauche = case_actuelle
                    case_actuelle.pere = cases[i][j-1]
                elif case_a_ouvrir == 1:
                    cases[i-1][j].fils_droite = case_actuelle
                    case_actuelle.pere = cases[i-1][j]

        self.entree = cases[0][0]
        self.sortie = cases[self.x-1][self.y-1]


    def afficher(self):
        """
        Affiche le labyrinthe gÃ©nÃ©rÃ© dans une fene^tre, en parcourant largeur
        Ne retourne rien
        """
        labyGraphique = LabyryntheGraphique(self.x, self.y)

        solution = self.solution()

        file = File()
        file.ajouterFile(self.entree)
        while not file.estVide():
            retrait = file.retirerFile()
            case = CaseGraphiqueLabyrinthe()
            if retrait.fils_droite == None:
                case.activer_mur_droit()
            if retrait.fils_gauche == None:
                case.activer_mur_bas()
            if retrait.valeur == (self.x-1, self.y-1):
                case.desactiver_mur_bas()
            if retrait.valeur in solution:
                case.colorier_en_rouge()

            labyGraphique.ajouterCaseGraphique(retrait.valeur[0], retrait.valeur[1], case)

            if retrait.fils_gauche != None:
                file.ajouterFile(retrait.fils_gauche)
            if retrait.fils_droite != None:
                file.ajouterFile(retrait.fils_droite)


        labyGraphique.afficher()

    def solution_recursif(self, debut, fin, chemin):
        """
        debut : Noeud de depart
        fin : Noeud de destination
        chemin : Variable stockant le chemin actuellement calculÃ©.
        Calcule un chemin allant du noeud "debut" vers le noeud "fin"
        Cet algorithme ressemble fortement Ã  celui utilisÃ© pour trouver un chemin dans un graphe.
        Retourne : La liste contenant successivement les coordonnÃ©es (tuples) des cases Ã  parcourir
        pour aller du noeud dÃ©but au noeud fin.
        Exemple : [(0,0), (1,0), (2,0), (2,1), etc...]
        """

        if self.entree == fin:
            chemin.insert(0, self.entree.valeur)
            return chemin

        chemin.insert(0, fin.valeur)
        return self.solution_recursif(self.entree, fin.pere, chemin)


    def solution(self):
        """
        Appelle la mÃ©thode rÃ©cursive "solution_recursif" afin de trovuer un chemin
        allant du noeud reprÃ©sentant l'entrÃ©e vers le noeud reprÃ©sentant la sortie.
        Retourne : La liste contenant successivement les coordonnÃ©es (tuples) des cases Ã  parcourir
        pour aller de l'entrÃ©e du labyrinthe Ã  la sortie de celui-ci.
        """
        return self.solution_recursif(self.entree, self.sortie, [])


#Votre programme "principal" ici

labirynthe = Labyrinthe(30, 30)
#afficher_arbre(labirynthe.entree)
labirynthe.afficher()
#print(labirynthe.solution())
