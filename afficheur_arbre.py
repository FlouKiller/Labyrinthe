import urllib.parse
import webbrowser

def traverser_arbre(arbre):
    queue = [(arbre, 0)]
    donnees_arbre = "digraph G { \n"
    numero = 0
    while len(queue) != 0:
        numero += 1
        courant = queue.pop(0)
        noeud_courant = courant[0]
        numero_parent = courant[1]
        if noeud_courant is None:
            donnees_arbre += "N%d [style=invis]\n" % (numero)
            donnees_arbre += "N%d -> N%d [style=invis]\n" % (numero_parent,numero)  
        else:
            donnees_arbre += "N%d [label=\"%s\"]\n" % (numero ,str(noeud_courant.valeur))
            queue.append((noeud_courant.fils_gauche, numero))
            queue.append((noeud_courant.fils_droite, numero))
            if numero_parent != 0:
                donnees_arbre += "N%d -> N%d\n" % (numero_parent,numero)  
    donnees_arbre += "}\n"
    return donnees_arbre
        
def generer_lien(arbre):
    donnees_formatees = urllib.parse.quote(traverser_arbre(arbre))
    lien_graphiz = "https://dreampuf.github.io/GraphvizOnline/#"+ donnees_formatees
    return lien_graphiz
  

def afficher_arbre(arbre):
    lien_arbre = generer_lien(arbre)
    webbrowser.open(lien_arbre)