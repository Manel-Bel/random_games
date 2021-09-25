import pygame 
import random
pygame.init()
from pygame.locals import *


WIN = pygame.display.set_mode((1000,700))
pygame.display.set_caption('MANDE BY MANEL')

rayon = 0
color =[(255 ,0 ,0) , (0 ,255 ,0) , (0 ,0 ,255) , (0 ,255 ,255) , (255 ,0 ,255) ,
(255 ,255 ,0) , (255 ,255 ,255), (152, 245, 255, 255), (142, 229, 238, 255), (122, 197, 205, 255), (83, 134, 139, 255),
(0, 0, 238, 255),(0, 0, 205, 255),(0, 0, 139, 255),(240, 248, 255), (160, 32, 240, 255),(155, 48, 255, 255),(145, 44, 238, 255),
(125, 38, 205, 255),(85, 26, 139, 255), (255, 0, 0, 255),(255, 0, 0, 255),(238, 0, 0, 255),(205, 0, 0, 255),(139, 0, 0, 255)]
def main_loop() :
    run = True
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False 
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                rayon = random.randint(5, 60)
                pygame.draw.circle(WIN, color[random.randint(0, len(color)-1)], event.pos, rayon, random.randint(0, 30))
            if event.type == MOUSEBUTTONDOWN and event.button == 3 :
                width = random.randint(5, 100)
                height = random.randint(5,100)
                pygame.draw.rect(WIN, color[random.randint(0, len(color)-1)], (event.pos[0], event.pos[1],width, height), random.randint(0, 30))
        pygame.display.update()
    pygame.quit()

main_loop()

