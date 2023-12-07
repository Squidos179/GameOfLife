from __future__ import annotations

import time

import pygame
from classes import Grille

sucess = False

def efface_ecran()->None:
    print("\u001B[H\u001B[J")

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
    print("Voulez-vous utiliser l'interface graphique ou l'interface terminal ?")
    print("1. Interface graphique \n 2. Interface terminal")
    try:
        choice = int(input("Votre choix : "))
        if choice != 1 and choice != 2:
            raise Exception
    except Exception:
        print("La valeur entrée est incorrecte.")
    else:
        sucess = True

running = True
clock = pygame.time.Clock()
if choice == 1:
    print("Appuyez sur 'Echap' pour fermer le programme")
    graph = Grille(l, h, pygame.display.set_mode((l * 10, h * 10)))
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        graph.jeu()
        graph.render_graph()
        pygame.display.flip()
        clock.tick(32)

if choice == 2:
    cmd = Grille(l, h)
    while(True):
        print("\u001B[H\u001B[3J")
        cmd.jeu()
        print(cmd)
        time.sleep(0.3)

pygame.quit()