from math import sqrt
import numpy as np
import pygame

class Cellule:
    def __init__(self, pos:list, vivant:bool) -> None:
        """
        Constructeur de la classe cellule
        Args : 
            pos : un tuple, représente le position de la cellule dans la grille
            vivant : un book, True si la cellule doit être vivante, False si elle est morte
        Return : 
            Ne retourne rien, c'est un constructeur
        """
        try:
            if type(pos) != list  or type(vivant) != bool:
                raise TypeError
        except TypeError as error:
            print(f"Au moins un des paramètres entrées pour la classe sont incorrects ! Plus de détails : {error}")
        else:
            self.actuel = vivant
            self.futur = False
            self.voisins = None
            self.civ = 0
            self.pos = pos

    def est_vivant(self):
        """
        Retourne l'état actuel d'une cellule (Vivante ou morte)
        Return : 
            Un booléen, True si la cellule est vivante, False si elle est morte
        """
        return self.actuel
    
    def set_voisins(self, list:list) -> None:
        """
        Donne à une cellule la liste de ses voisins
        Args : 
            list : une liste d'objet de type Cellule
        Return :
            Rien, on change juste l'attribut voisin d'une cellule
        """
        try:
            if type(list) != list:
                raise TypeError
        except TypeError as error:
            print(f"Les paramètres d'entrées sont incorrects ! Plus de détails : {error}")
        else:
            self.voisins = list

    def get_voisins(self):
        """
        Retourne la liste des voisins d'une cellule
        Return : 
            Une liste d'objets de type Cellule
        """
        return self.voisins
    
    def naitre(self) -> None:
        """
        Change l'état futur d'une voisine à True (vivante)
        """
        self.futur = True

    def mourir(self) -> None:
        """
        Change l'état futur d'une voisine à False (Morte)
        """
        self.futur = False

    def basculer(self):
        """
        Change l'état futur d'une voisine à son état actuel
        """
        self.futur = self.actuel
    
    def __repr__(self) -> str:
        """
        Retourne la réprésentation d'une cellule
        Return : 
            Un string, 'x' si la cellule est vivante, '-' si elle est morte
        """
        if self.est_vivant():
            return "x"
        else:
            return "-"

    def __str__(self) -> str:
        """
        Retourne la représentation d'une cellule en voulant l'afficher avec un print()
        Return : 
            Un string, celui que renvoie le __repr__()
        """
        return self.__repr__()
        
    def calcule_etat_futur(self)-> None:
        """
        Calcule l'état futur d'une cellule en fonction de ses voisins qui sont vivants ou morts
        """
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
        """
        Fait le rendu de la cellule dans la fenêtre pygame en fonction de son état (vivant ou mort) et de sa position
        """
        if self.est_vivant():
            pygame.draw.rect(scr, (0, 0, 0), pygame.Rect(self.pos[0] * 10, self.pos[1] * 10, 10, 10))
        else:
            pygame.draw.rect(scr, (255, 255, 255), pygame.Rect(self.pos[0] * 10, self.pos[1] * 10, 10, 10))

class Grille:

    def __init__(self, longueur:int, hauteur:int) -> None:
        """
        Constructeur de la classe Grille
        Args : 
            longueur : un entier qui doit être un multiple de 10
            hauteur : un entier qui doit être un multiple de 10
        Return :
            Rien, c'est un constructeur
        """
        try:
            if type(longueur) != int or type(hauteur) != int:
                raise TypeError
        except TypeError:
            print(f"Au moins un des paramètres entrées pour la classe sont incorrects !")
        else:
            self.largeur = longueur
            self.hauteur = hauteur
            self.matrix = [[Cellule([x, y], self.remplir_alea(0.2)) for x in range(self.largeur)] for y in range(self.hauteur)]
            self.civ = 0
            self.i = 0

    def __repr__(self) -> str:
        """
        Donne la réprésentation d'une Grille de cellule
        Return : 
            Un string des différentes représentation de chaque cellule de la grille
        """
        feur = ""
        for i in range(self.hauteur):
            for p in range(self.largeur):
                feur += str(self.matrix[i][p])
            feur += "\n"
        return feur

    def __str__(self) -> str:
        """
        Donne la représentation d'une cellule quand on veut l'afficher depuis un print()
        """
        return self.__repr__()

    def dans_grille(self, i, j):
        """
        Nous informe si une position donnée est aussi une position d'une des cellules de la grille
        Args : 
            i : un entier
            j : un entier
        Return : 
            Un booléen, True si la position donnée correspond à une cellule de la grille, False si ce n'est pas le cas
        """
        try:
            if type(i) != int or type(j) != int:
                raise TypeError
        except TypeError:
            print(f"Les coordonnées entrées en paramètres ne sont pas bonnes")
        else:
            if i < self.hauteur and i >= 0 and j < self.largeur and j >= 0:
                if type(self.matrix[i][j]) != Cellule:
                    return False
                else:
                    return True
            else:
                return False
        
    def setXY(self, i, j, modif):
        """
        Modifie l'état futur d'une cellule de la grille
        Args :
            i : un entier, l'abscisse de la cellule qu'on veut modifier
        """
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
        return bool(choice[0])
    
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
    clock.tick(32)
pygame.quit()