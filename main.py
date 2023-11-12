from math import sqrt
import numpy as np

class Cellule:

    def __init__(self) -> None:
        self.actuel = False
        self.futur = False
        self.voisins = None
        self.civ = 0

    def est_vivant(self):
        return self.actuel
    
    def set_voisins(self, list) -> None:
        self.voisins = list

    def get_voisins(self):
        return self.voisins
    
    def naitre(self):
        self.futur = True

    def mourir(self):
        self.futur = False

    def basculer(self):
        self.futur = self.actuel
    
    def __repr__(self) -> str:
        if self.est_vivant():
            return "x"
        else:
            return "-"

    def __str__(self) -> str:
        return self.__repr__()
        
    def calcule_etat_futur(self):
        self.civ = 0
        for i in self.voisins:
            if i.actuel == True:
                self.civ += 1
        if self.civ > 3 and self.est_vivant():
            self.mourir()
        if self.civ > 3 and self.est_vivant() == False:
            self.mourir()
        if self.civ == 3 and self.est_vivant() == False:
            self.naitre()
        if self.civ == 3 and self.est_vivant():
            self.naitre()
        if self.civ == 2 and self.est_vivant():
            self.naitre()
        if self.civ == 2 and self.est_vivant == False:
            self.naitre()
        if self.civ < 2 and self.est_vivant():
            self.mourir()
        if self.civ < 2 and self.est_vivant() == False:
            self.mourir()
        

class Grille:
    
    def __init__(self, largeur, hauteur) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrix = [[Cellule() for x in range(self.largeur)] for y in range(self.hauteur)]

    def __repr__(self) -> str:
        feur = ""
        for i in range(self.hauteur):
            for p in range(self.largeur):
                feur += str(self.matrix[i][p])
            feur += "\n"
        return feur

    def __str__(self) -> str:
        return self.__repr__()

    def dans_grille(self, i, j):
        if i < self.hauteur and i >= 0 and j < self.largeur and j >= 0:
            if type(self.matrix[i][j]) != Cellule:
                return False
            else:
                return True
        else:
            return False
        
    def setXY(self, i, j, modif):
        if self.dans_grille():
            self.matrix[i][j].futur = modif
        else:
            print("Cette cellule n'est pas dans la grille")

    def getXY(self, i, j):
        if self.dans_grille():
            return self.matrix[i][j]
        else:
            print("Cette cellule n'est pas dans la grille")
    
    def get_largeur(self):
        return self.largeur
    
    def get_hauteur(self):
        return self.hauteur
        
    def est_voisin(self, i, j, x, y):
        if self.dans_grille(x, y):
            if self.dans_grille(i, j):
                if 0 < sqrt((i - x)**2 + (j - y)**2) <= sqrt(2):
                    return True
                else:
                    return False
        
    def get_voisins(self, i, j):
        neighboor = []
        for n in range(-1, 2):
            for p in range(-1, 2):
                if self.est_voisin(i, j, i + n, j + p):
                    neighboor.append(self.matrix[i + n][j + p])
        return neighboor

    def affecte_voisins(self):
        for i in range(self.hauteur):
            for n in range(self.largeur):
                self.matrix[i][n].voisins = self.get_voisins(i, n)

    def remplir_alea(self, jaaj):
        choice = np.random.choice([True, False], 1, p=[jaaj, 1 - jaaj])
        return choice[0]
    
    def jeu(self): 
            while(True):
                print(feur.matrix[2][1].est_vivant())
                print(self)
                f = input("Suite")
                print("\u001B[H\u001B[J")
                self.affecte_voisins()
                for i in range(self.hauteur):
                    for p in range(self.largeur):
                        self.matrix[i][p].calcule_etat_futur()
                for i in range(self.hauteur):
                    for p in range(self.largeur):
                        self.matrix[i][p].actuel = self.matrix[i][p].futur
                
feur = Grille(100, 10)
feur.matrix[2][1].actuel = True
feur.matrix[2][2].actuel = True
feur.matrix[2][3].actuel = True
feur.matrix[2][4].actuel = True
feur.matrix[3][0].actuel = True
feur.matrix[3][4].actuel = True
feur.matrix[4][4].actuel = True
feur.matrix[5][0].actuel = True
feur.matrix[5][3].actuel = True
feur.jeu()