import pygame
from pygame . locals import * # Permet de charger des constantes comme

from random import randint
taille = largeur , hauteur = 1500 , 850 # Taille de la fenêtre graphique
couleurs = [(255 ,0 ,0) , (0 ,255 ,0) , (0 ,0 ,255) , (0 ,255 ,255) , (255 ,0 ,255) ,(255 ,255 ,0) , (255 ,255 ,255) ]
pygame.init() # Initialisation de tous les modules pygame .

fenetre = pygame.display.set_mode( taille )
continuer = True
while continuer :
    for event in pygame.event.get() : #On parcourt tous les événements
        if event.type == QUIT : #Si c’est un événement de fermeture de
            continuer = False
        if event.type == MOUSEBUTTONDOWN and event . button ==1: #Si c’est
            rayon = randint (5 ,50) # rayon aléatoire
            ep = randint(0, 30)
            couleur = couleurs [ randint (0 , 6) ] # couleur aléatoire
            pygame.draw.circle( fenetre , couleur , event .pos , rayon , ep)
    
        pygame.display.flip () # Mise à jour de l’affichage en affichant le
        
pygame . quit ()
