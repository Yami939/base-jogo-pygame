import pygame
from pygame.locals import*
from sys import exit

largura = 640
altura = 480

branco = (255,255,255)
preto = (0,0,0)

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('rundinozauro')

class nome(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass
    
todas_as_sprites = pygame.sprite.Group()
dino = (nome)
todas_as_sprites.add(nome)

relogio = pygame.sprite.Group()
while true:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        pygame.quit()
        exit()
        
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    
    pygame.display.flip()