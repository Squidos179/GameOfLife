from __future__ import annotations
import time
from classes import Grille
sucess = False
load = None
try:
    import pygame
except:
    print("Pygame n'est pas présent sur votre interpreteur Python ou n'a pas pu être chargé.")
    print("Il sera donc impossible d'utiliser la partie graphique du programme.")
    load = None
    choice = 2
else:
    load = True

while sucess == False:
    print("Veuillez entrer les dimensions de la grille, elles doivent être toutes les deux des multiples de 10 et des entiers")
    try:
        l = int(input("Veuillez entrer la longueur de la grille : "))
        h = int(input("Veuillez entrer la hauteur de la grille : "))
        if l % 10 != 0 or h % 10 != 0 or type(l) != int or type(h) != int:
            raise Exception
    except Exception:
        print("Les valeurs entrées ne sont pas bonnes, veuillez réessayer.")
    else:
        sucess = True

sucess = False

while sucess == False:
    print("Le taux de remplissage représentera le taux de cellule vivante dans la grille, merci donner un compris entre 0 et 1.")
    try:
        taux = float(input("Veuillez choisir le taux de remplissage : "))
        if taux > 1 or taux < 0 or type(taux) != float:
            raise Exception
    except Exception:
        print("Le taux entré est incrorrect, veuillez réessayer.")
    else:
        sucess = True

sucess = False

if load == True:
    while sucess == False:
        print("Voulez-vous utiliser l'interface graphique ou l'interface terminal ?")
        print("1. Interface graphique \n2. Interface terminal")
        try:
            choice = int(input("Votre choix : "))
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("La valeur entrée est incorrecte.")
        else:
            sucess = True

running = True
if choice == 1:
    clock = pygame.time.Clock()
    print("Appuyez sur 'Echap' pour fermer le programme")
    graph = Grille(l, h, taux, pygame.display.set_mode((l * 10, h * 10)))
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        graph.render_graph()
        graph.jeu()
        pygame.display.flip()
        clock.tick(16)
    pygame.quit()

if choice == 2:
    cmd = Grille(l, h, taux)
    while(True):
        print("\u001B[H\u001B[3J")
        print(cmd)
        cmd.jeu()
        time.sleep(0.3)
