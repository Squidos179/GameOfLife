from math import sqrt
import numpy as np
import pygame

class Cellule:
    def __init__(self, pos, vivant) -> None:
        self.actuel = vivant
        self.futur = False
        self.voisins = None
        self.civ = 0
        self.pos = pos

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
        
    def render(self):
        if self.est_vivant():
            pygame.draw.rect(scr, (0, 0, 0), pygame.Rect(self.pos[0] * 10, self.pos[1] * 10, 10, 10))
        else:
            pygame.draw.rect(scr, (255, 255, 255), pygame.Rect(self.pos[0] * 10, self.pos[1] * 10, 10, 10))
class Grille:
    
    def __init__(self, longueur, hauteur) -> None:
        self.largeur = longueur
        self.hauteur = hauteur
        self.matrix = [[Cellule((x, y), self.remplir_alea(0.2)) for x in range(self.largeur)] for y in range(self.hauteur)]
        self.civ = 0
        self.i = 0

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
            self.affecte_voisins()
            for i in range(self.hauteur):
                for p in range(self.largeur):
                    self.matrix[i][p].calcule_etat_futur()
            for i in range(self.hauteur):
                for p in range(self.largeur):
                    self.matrix[i][p].actuel = self.matrix[i][p].futur

    def render(self):
        self.civ = 0
        for i in range(self.hauteur):
            for p in range(self.largeur):
                self.matrix[i][p].render()
                if self.matrix[i][p].actuel:
                    self.civ += 1
        self.i += 1
        print(self.civ, self.i)


l = int(input("Veuillez entrer la longueur de la grille : "))
h = int(input("Veuillez entrer la hauteur de la grille : "))

scr = pygame.display.set_mode((l*10, h*10))
feur = Grille(l, h)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    feur.jeu()
    feur.render()
    pygame.display.flip()
    clock.tick(5)
pygame.quit()