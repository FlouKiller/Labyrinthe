from File import File
from afficheur_arbre import afficher_arbre

class NoeudBinaire:
    def __init__(self, valeur, fils_gauche, fils_droit):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droite = fils_droit
        self.pere = None

    def est_feuille(self):
        return self.fils_droite is None and self.fils_gauche is None

    def hauteur(self):
        h_gauche = 0
        h_droite = 0
        if self.fils_gauche != None:
            h_gauche = self.fils_gauche.hauteur()
        if self.fils_droite != None:
            h_droite = self.fils_droite.hauteur()
        return 1 + max(h_gauche, h_droite)

    def taille(self):
        taille = 1
        if self.fils_gauche != None:
            taille += self.fils_gauche.taille()
        if self.fils_droite != None:
            taille += self.fils_droite.taille()
        return taille

    def nombre_feuilles(self):
        if self.est_feuille():
            return 1
        else:
            somme = 0
            if self.fils_gauche:
                somme += self.fils_gauche.nombre_feuilles()
            if self.fils_droite:
                somme += self.fils_droite.nombre_feuilles()
            return somme

    def parcours_infixe(self):
        if self.fils_gauche != None:
            self.fils_gauche.parcours_infixe()
        print(self.valeur)
        if self.fils_droite != None:
            self.fils_droite.parcours_infixe()

    def parcours_prefixe(self):
        print(self.valeur)
        if self.fils_gauche != None:
            self.fils_gauche.parcours_prefixe()
        if self.fils_droite != None:
            self.fils_droite.parcours_prefixe()

    def parcours_suffixe(self):
        if self.fils_gauche != None:
            self.fils_gauche.parcours_suffixe()
        if self.fils_droite != None:
            self.fils_droite.parcours_suffixe()
        print(self.valeur)

    def parcours_largeur(self):
        f = File()
        f.ajouterFile(self)
        while not(f.estVide()):
            noeud_courant = f.retirerFile()
            print(noeud_courant.valeur)
            if noeud_courant.fils_gauche != None:
                f.ajouterFile(noeud_courant.fils_gauche)
            if noeud_courant.fils_droite != None:
                f.ajouterFile(noeud_courant.fils_droite)

    def parcours_infixe_liste(self):
        l = []
        if self.fils_gauche != None:
            l.extend(self.fils_gauche.parcours_infixe_liste())
        l.append(self.valeur)
        if self.fils_droite != None:
            l.extend(self.fils_droite.parcours_infixe_liste())
        return l

E = NoeudBinaire("E", None, None)
C = NoeudBinaire("C", None, E)
D = NoeudBinaire("D", None, None)
B = NoeudBinaire("B", C, D)
I = NoeudBinaire("I", None, None)
G = NoeudBinaire("G", I, None)
J = NoeudBinaire("J", None, None)
H = NoeudBinaire("H", None, J)
F = NoeudBinaire("F", G, H)
A = NoeudBinaire("A", B, F)
arbre = A