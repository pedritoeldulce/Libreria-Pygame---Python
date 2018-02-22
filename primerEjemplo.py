import pygame # libreria de funciones de pygame
from math import pi
from math import cos
from math import sin

pygame.init() # inicializamos el motor de juegos

#definimos colores - RGB
BLANCO = (255,255,255)  #color blanco
VERDE = (0,150,0) # color verde
BLACK = (0,0,0)
dimension = (600, 400) # dimension de la pantalla (horiz, vert)

pantalla= pygame.display.set_mode(dimension) # abrimos la pantalla con la dimension establecida
# set_mode -> inicializa una ventana con las dimensiones

pygame.display.set_caption("Primer Ventana hecho con Pygame")
# set_caption -> titulo de la ventana

## Interaccion con el Usuario

hecho=False # bandera

reloj = pygame.time.Clock() #Creamos un reloj
#para gestionar la velocidad con la que se actualiza la pantalla

while not hecho:
    for evento in pygame.event.get(): # captura todos los eventos del usuario
        if evento.type == pygame.QUIT:
            print("hizo click en SALIR")
            hecho=True
            
        elif  evento.type == pygame.MOUSEBUTTONDOWN:
            print("Esta presionando el raton")
        elif evento.type == pygame.MOUSEBUTTONUP:
            print("Ha soltado el raton")
            #hecho = True



    pantalla.fill(BLANCO)#llenamos(pintamos) la pantalla cada vez que se actualiza

    #dibuja un circulo (pantalla, color, (x,y),radio,ancho de linea)
    #pygame.draw.circle(pantalla, VERDE, (40,40),40,0 )

    #dibuja una linea (MAS fina)
    #pygame.draw.aaline(pantalla, VERDE, [0, 0],[50, 80],True)

    #DUBUJA UNA LINEA (CONJUNTO)
    #pygame.draw.line(pantalla, VERDE, [0, 0], [50,30], 1)

    #Dibuja una rectangulo (x,y,x+a,y+b)
    #pygame.draw.rect(pantalla, VERDE, [75, 10, 100, 80], 1)

    #dibuja un poligono [[un punto] , []]
    #pygame.draw.polygon(pantalla, VERDE, [[100, 100], [0, 200], [200, 200]], 1)

    #dibuja una arco
##    pygame.draw.arc(pantalla, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
##    pygame.draw.arc(pantalla, VERDE,[210, 75, 150, 125], pi/2, pi, 2)
##    pygame.draw.arc(pantalla, BLACK, [210, 75, 150, 125], pi,3*pi/2, 2)
##    pygame.draw.arc(pantalla, VERDE,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)


    

    #desplazamiento vertivcal
    #for desplazar_y in range(0, 100, 10):
    #    pygame.draw.line(pantalla,VERDE, [50, 50 + desplazar_y], [100, 50 + desplazar_y], 2)
    
        
    # escribien texto en pantalla
    
    fuente = pygame.font.Font(None,25)

    texto = fuente.render("HOLA MUNDO",True, BLACK)
    pantalla.blit(texto,[250,250])
    numero=28
    texto = fuente.render("Numero :"+ str(numero), True, BLACK)


    pygame.draw.ellipse(pantalla, VERDE, [20, 20, 450, 100], 2)

    
    pygame.display.flip()#actualiza la pantalla, muestra todo lodibujado hasta el momento
    
    reloj.tick(20) # fotogramas por segundo
            
        




pygame.quit() #cierra programa
