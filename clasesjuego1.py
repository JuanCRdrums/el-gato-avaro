import pygame
import random

ALTO = 700
ANCHO = 700
CENTRO = [ANCHO/2,ALTO/2]





def cut(archivo, an , al):
    fondo = pygame.image.load(archivo).convert_alpha()
    info = fondo.get_size()
    img_ancho = info[0]  #alto y ancho de cada sprite
    img_alto = info[1]
    corte_x = img_ancho /an
    corte_y = img_alto/al

    m = []
    for i in range(an):
        fila = []
        for j in range(al):
            cuadro = [i*corte_x,j*corte_y,corte_x,corte_y]
            recorte = fondo.subsurface(cuadro)
            fila.append(recorte)
        m.append(fila)
    return m








class Jugador(pygame.sprite.Sprite):

    def __init__(self,imgSprite):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.dir = 0
        self.i = 0
        self.dx = 0
        self.dy = 0
        self.montado = False
        self.vidas = 20
        self.puntos = 0
        self.win1 = False
        self.sound = pygame.mixer.Sound("gato.ogg")

    def update(self):
        if self.dx != 0 or self.dy != 0:
            if self.i < 2:
                self.i += 1
            else:
                self.i = 0
        self.image = self.m[self.i][self.dir]
        if self.rect.right <= ANCHO and self.rect.left >= 0:
        	self.rect.x += self.dx

        if self.rect.right >= ANCHO and self.dx < 0:
        	self.rect.x += self.dx

        if self.rect.left <= 0 and self.dx > 0:
        	self.rect.x += self.dx

        if self.rect.top >= 0 and self.rect.bottom <= ALTO:
        	self.rect.y += self.dy

        if self.rect.top <= 0 and self.dy > 0:
        	self.rect.y += self.dy

        if self.rect.bottom >= ALTO and self.dy < 0:
        	self.rect.y += self.dy

        if self.rect.bottom > ALTO:
        	self.vidas -= 1
        	self.sound.play()


        self.gravity()


    def gravity(self):

    	if self.dy >= 0:
    		self.dy += 1.5

    	if self.rect.bottom >= ALTO:
    		self.dy = 0
    		self.rect.bottom = ALTO





class Log(pygame.sprite.Sprite):

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.dx = 0


    def update(self):

    	self.rect.x += self.dx
    	if self.rect.right <= 0 and self.dx < 0:
    		self.rect.left = ANCHO
    	if self.rect.left >= ANCHO and self.dx > 0:
    		self.rect.right = 0



class Moneda(pygame.sprite.Sprite):

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()


class Corazon(pygame.sprite.Sprite):

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()


