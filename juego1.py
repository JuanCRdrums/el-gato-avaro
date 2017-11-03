import pygame
import random
from clasesjuego1 import *

ALTO = 700
ANCHO = 700
CENTRO = [ANCHO/2,ALTO/2]

BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]







if (__name__ == '__main__'):
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    general = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    logs = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    hearts = pygame.sprite.Group()
    cuts = cut("animales.png",12,8)
    jugador = Jugador(cuts)
    jugador.rect.x = CENTRO[0]
    jugador.rect.bottom = ALTO
    en = False
    tasa = 30
    time = 0
    win = False
    inicio = True


    general.add(jugador)
    jugadores.add(jugador)
    k = 0
    for i in range(100,600,220):
    	nc = Moneda("moneda.png")
    	nc.rect.y = i - 32
    	nc.rect.x = random.randrange(0,ANCHO-32)
    	coins.add(nc)
    	general.add(nc)

    	nh = Corazon("corazon.png")
    	nh.rect.y = i - 32
    	nh.rect.x = random.randrange(0,ANCHO-32)
    	hearts.add(nh)
    	general.add(nh)



    	r = random.randrange(0,2)
    	for j in range(3):
    		if j == r:
    			nc1 = Moneda("moneda.png")
    			nc1.rect.y = random.randrange(0,ALTO - 32)
    			nc1.rect.x = random.randrange(0,ANCHO - 32)
    			coins.add(nc1)
    			general.add(nc1)
    		nLog = Log("log-1.png")
    		nLog.rect.y = i
    		nLog.rect.x = j*200
    		if(k % 2 == 0):
    			nLog.dx = 5
    		else:
    			nLog.dx = -5
    		logs.add(nLog)
    		general.add(nLog)



    	k += 1


    nivel2 = False
    nivel1 = True



    clock = pygame.time.Clock()
    pygame.display.flip()
    cont = 0
    fin=False
    pause = False
    nivel = 1
    jugador2 = Jugador(cuts)
    jugadores2 = pygame.sprite.Group()
    general2 = pygame.sprite.Group()
    logs2 = pygame.sprite.Group()
    coins2 = pygame.sprite.Group()
    hearts2 = pygame.sprite.Group()

    loss = False

    soundJump = pygame.mixer.Sound("jump.ogg")
    coinSound = pygame.mixer.Sound("Coin.ogg")
    lifeSound = pygame.mixer.Sound("vida.ogg")




    while not fin:

    	cont += 1

    	segundos = time // tasa
    	minutos = 0

    	time += 1
    	if segundos == 30:
    		segundos = 0
    		time = 0
    		if nivel1:
    			jugador.vidas -= 1
    		if nivel2:
    			jugador2.vidas -= 1

    	texto_reloj ='{0:02}:{1:02}'.format(minutos,segundos)

    	if jugador.dy < 0 and cont == 15 and nivel1:
    		cont = 0
    		jugador.dy = 0

    	if jugador2.dy < 0 and cont == 15 and nivel2:
    		cont = 0
    		jugador2.dy = 0

    	if jugador.rect.bottom == ALTO and nivel1:
    		en = True

    	if jugador2.rect.bottom == ALTO and nivel2:
    		en = True
    	"""else:
    		en = False"""



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_SPACE and en:
                	cont = 0
                	soundJump.play()
                	if nivel1:
	                    jugador.dir = 3
	                    jugador.dy = -15
	                    jugador.dx = 0
	                else:
	                	jugador2.dir = 3
	                	jugador2.dy = -15
	                	jugador2.dx = 0

                if event.key == pygame.K_RIGHT:
                	if nivel1:
                		if jugador.rect.bottom == ALTO:
                			jugador.dir = 2
                			jugador.dx = 15

                	else:
                		if jugador2.rect.bottom == ALTO:
                			jugador2.dir = 2
                			jugador2.dx = 15

                if event.key == pygame.K_LEFT:
                	if nivel1:
                		if jugador.rect.bottom == ALTO:
                			jugador.dir = 1
                			jugador.dx = -15
                	else:
                		if jugador2.rect.bottom == ALTO:
                			jugador2.dir = 1
                			jugador2.dx = -15

                if event.key == pygame.K_p:
                	if pause:
                		pause = False
                	else:
                		pause = True


                if event.key == pygame.K_i:
                	if inicio:
                		inicio = False

                if event.key == pygame.K_c:
                	if jugador.win1:
                		nivel2 = True
                		nivel = 2
                		jugador2.rect.x = CENTRO[0]
                		jugador2.rect.bottom = ALTO
                		jugador2.vidas = jugador.vidas
                		jugador2.puntos = jugador.puntos

                		general2.add(jugador2)
                		jugadores2.add(jugador2)
                		k = 0
                		for i in range(100,600,220):
                			nc = Moneda("moneda.png")
                			nc.rect.y = i - 32
                			nc.rect.x = random.randrange(0,ANCHO-32)
                			coins2.add(nc)
                			general2.add(nc)

                			nh = Corazon("corazon.png")
                			nh.rect.y = i - 32
                			nh.rect.x = random.randrange(0,ANCHO - 32)
                			hearts2.add(nh)
                			general2.add(nh)

                			r = random.randrange(0,2)
                			for j in range(3):
                				if j == r:
                					nc1 = Moneda("moneda.png")
                					nc1.rect.y = random.randrange(0,ALTO - 32)
                					nc1.rect.x = random.randrange(0,ANCHO - 32)
                					coins2.add(nc1)
                					general2.add(nc1)
                				nLog = Log("log-1.png")
                				nLog.rect.y = i
                				nLog.rect.x = j*200
                				if(k % 2 == 0):
                					nLog.dx = 10
                				else:
                					nLog.dx = -10

					    		logs2.add(nLog)
					    		general2.add(nLog)



					    	k += 1






            if event.type == pygame.KEYUP:
            	if nivel1:
            		jugador.dx = 0
            		if jugador.dy < 0:
            			jugador.dy = 0
            			jugador.dx = 0
            			en = False
            			cont = 0
            	else:
            		jugador2.dx = 0
            		if jugador2.dy < 0:
            			jugador2.dy = 0
            			jugador2.dx = 0
            			en = False
            			cont = 0


        lCol = pygame.sprite.spritecollide(jugador,logs,False)
        for i in lCol:
            if jugador.dy > 0 and jugador.rect.top <= i.rect.top:
            	jugador.rect.bottom = i.rect.top
            	jugador.montado = True
            	jugador.dy = 0
            	jugador.dx = i.dx
            	en = True


            if jugador.dy < 0 and jugador.montado == False:
            	jugador.rect.top = i.rect.bottom

            if jugador.dy < 0 and jugador.montado:
            	jugador.dx = 0
            	jugador.montado = False


        lCol = pygame.sprite.spritecollide(jugador,coins,True)
        for i in lCol:
        	jugador.puntos += 1
        	coinSound.play()


        lCol = pygame.sprite.spritecollide(jugador2,logs2,False)
        for i in lCol:
            if jugador2.dy > 0 and jugador2.rect.top <= i.rect.top:
            	jugador2.rect.bottom = i.rect.top
            	jugador2.montado = True
            	jugador2.dy = 0
            	jugador2.dx = i.dx
            	en = True


            if jugador2.dy < 0 and jugador2.montado == False:
            	jugador2.rect.top = i.rect.bottom

            if jugador2.dy < 0 and jugador2.montado:
            	jugador2.dx = 0
            	jugador2.montado = False


        lCol = pygame.sprite.spritecollide(jugador2,coins2,True)
        for i in lCol:
        	jugador2.puntos += 1
        	coinSound.play()

        lCol = pygame.sprite.spritecollide(jugador,hearts,True)
        for i in lCol:
        	jugador.vidas += 1
        	lifeSound.play()

        lCol = pygame.sprite.spritecollide(jugador2,hearts2,True)
        for i in lCol:
        	jugador2.vidas += 1
        	lifeSound.play()




        if jugador.puntos == 6:
        	jugador.win1 = True
        	nivel1 = False

        if jugador2.puntos == 12:
        	win = True

        if jugador.vidas == 0 or jugador2.vidas == 0:
        	loss = True



        pantalla.fill(NEGRO)

        if not pause and not jugador.win1 and not loss and not win and not inicio:
        	general.update()
	        msVidas = "Vidas: " + str(jugador.vidas)
	        font = pygame.font.SysFont("comicsansms",30)
	        image = font.render(msVidas,1,BLANCO)
	        pantalla.blit(image,[0,0])


	        msPuntos = "Puntos: " + str(jugador.puntos)
	        image = font.render(msPuntos,1,BLANCO)
	        pantalla.blit(image,[130,0])
	        msN1 = "Nivel: " + str(nivel)
	        image = font.render(msN1,1,BLANCO)
	        pantalla.blit(image,[300,0])
	        image = font.render(texto_reloj,1,BLANCO)
	        pantalla.blit(image,[500,0])

	        general.draw(pantalla)
        elif pause:
        	msPause = "PAUSA"
        	font = pygame.font.SysFont("comicsansms",60)
        	image2 = font.render(msPause,1,ROJO)
        	pantalla.blit(image2,[300,CENTRO[1]])
        elif jugador.win1 and not nivel2:
        	msWin1 = "NIVEL 1 COMPLETADO"
        	msContinue1 = "Para continuar presione la tecla C"
        	font1 = pygame.font.SysFont("comicsansms",60)
        	imageW1 = font1.render(msWin1,1,ROJO)
        	font2 = pygame.font.SysFont("comicsansms",30)
        	imagenC1 = font2.render(msContinue1,1,BLANCO)
        	pantalla.blit(imageW1,[200,300])
        	pantalla.blit(imagenC1,[200,400])

        elif nivel2 and not loss and not win and not inicio:
        	general2.update()
        	msVidas = "Vidas: " + str(jugador2.vidas)
        	font = pygame.font.SysFont("comicsansm",30)
        	image = font.render(msVidas,1,BLANCO)
        	pantalla.blit(image,[0,0])

        	msPuntos = "Puntos: " + str(jugador2.puntos)
        	image = font.render(msPuntos,1,BLANCO)
        	pantalla.blit(image,[130,0])
        	msN2 = "Nivel: " + str(nivel)
        	image = font.render(msN2,1,BLANCO)
        	pantalla.blit(image,[300,0])
        	image = font.render(texto_reloj,1,BLANCO)
        	pantalla.blit(image,[500,0])
        	general2.draw(pantalla)

        elif loss:
        	fin = True
        	msg = "PERDISTE"
        	font = pygame.font.SysFont("comicsansms",60)
        	image2 = font.render(msg,1,ROJO)
        	pantalla.blit(image2,[300,CENTRO[1]])


        elif win:
        	fin = True
        	msg = "GANASTE"
        	font = pygame.font.SysFont("comicsansms",60)
        	image2 = font.render(msg,1,ROJO)
        	pantalla.blit(image2,[300,CENTRO[1]])

        elif inicio:
        	msg1 = "GATO AVARO"
        	msg2 = "Bienvenido a EL GATO AVARO"
        	msg3 = "Debes agarrar todas las monedas en los dos niveles para ganar"
        	msg4 = "Cada vez que caigas al piso perderas una vida"
        	msg5 = "Cada vez que pasen 30 segundos perderas una vida"
        	msg6 = "Puedes pausar el juego pulsando la tecla p"
        	msg7 = "Empiezas con 20 vidas. Si se te acaban, pierdes"
        	msg8 = "Para aumentar una vida, puedes agarrar un corazon"
        	msg9 = "Mueves hacia los lados con las flechas laterales"
        	msg10 = "Solo te puedes mover a los lados cuando estas en el piso"
        	msg11 = "Para saltar, presiona la barra espaciadora"
        	msg12 = "Para iniciar, presiona la tecla I"
        	font1 = pygame.font.SysFont("comicsansms",60)
        	font2 = pygame.font.SysFont("comicsansms",30)
        	img1 = font1.render(msg1,1,ROJO)
        	img2 = font2.render(msg2,1,BLANCO)
        	img3 = font2.render(msg3,1,BLANCO)
        	img4 = font2.render(msg4,1,BLANCO)
        	img5 = font2.render(msg5,1,BLANCO)
        	img6 = font2.render(msg6,1,BLANCO)
        	img7 = font2.render(msg7,1,BLANCO)
        	img8 = font2.render(msg8,1,BLANCO)
        	img9 = font2.render(msg9,1,BLANCO)
        	img10 = font2.render(msg10,1,BLANCO)
        	img11 = font2.render(msg11,1,BLANCO)
        	img12 = font2.render(msg12,1,BLANCO)
        	pantalla.blit(img1,[200,0])
        	pantalla.blit(img2,[0,100])
        	pantalla.blit(img3,[0,150])
        	pantalla.blit(img4,[0,200])
        	pantalla.blit(img5,[0,250])
        	pantalla.blit(img6,[0,300])
        	pantalla.blit(img7,[0,350])
        	pantalla.blit(img8,[0,400])
        	pantalla.blit(img9,[0,450])
        	pantalla.blit(img10,[0,500])
        	pantalla.blit(img11,[0,550])
        	pantalla.blit(img12,[0,600])







        pygame.display.flip()
        clock.tick(tasa)
