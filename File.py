from Cellule import Cellule

class File:
    
    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0
        
    def estVide(self):
        return self.tete == None
    
    def valeurTete(self):
        if not(self.estVide()):
            return self.tete.valeur
        else:
            return None
    
    def ajouterFile(self, x):
        dernierElement = Cellule(x, None)  
        if(self.estVide()):
            self.tete = dernierElement
        else:
            self.queue.suivant = dernierElement
        self.queue = dernierElement
        self.taille += 1
        
    def retirerFile(self):
        if not(self.estVide()):
            valeur = self.tete.valeur
            self.tete = self.tete.suivant
            self.taille -= 1
            return valeur
        else:
            return None
        
    def __len__(self):
        return self.taille