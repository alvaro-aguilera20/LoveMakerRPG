import sqlite3 as sql

import pygame

pygame.init()

pygame.font.Font()

#definir graficos que sacamos de la carpeta graficos
cielo = pygame.image.load("graficos/cielo.png")
edificiosDeFondo = pygame.image.load("graficos/edificios.png")
jefecitoEnfadadito = pygame.image.load("graficos/jefe.png")
humano = pygame.image.load("graficos/Humano.png")

#definir colores
negro = (0,0,0)
rojo = (255,0,0)
verde_lima = (70,255,0)
azul = (0,43,255)
blanco = (255,255,255)
pielBronceada = (255,191,71)
dorado = (255, 215, 0)
gris = (128,128,128)
plateado = (192,192,192)
oxido = (183,65,14)
rosaOscuro = (218,44,67)
celeste = (81,209,246)
celestePastel = (121,210,230)
amarillo = (253,253,150)

pantalla=pygame.display.set_mode((1280,720))
pygame.display.set_caption("ventana basica")

#definir fuentes tipograficas

FArial = pygame.font.SysFont("Arial", 50)
FTimes = pygame.font.SysFont("times",100)
FPapyro = pygame.font.SysFont("Papyrus", 50)
FCalacaChida = pygame.font.SysFont("comic sans", 50)
Flucida = pygame.font.SysFont("lucida sans typewritter",100)
FOCR = pygame.font.SysFont("OCR A EXTENDED",100)
FOCRM = pygame.font.SysFont("OCR A EXTENDED",50)

def mostrarTexto(texto, fuente, color, X, Y):
    Text= fuente.render(texto, True, color)
    pantalla.blit(Text,(X,Y))

class boton():
    def __init__(BE,imagen, x, y,font,texto):
        BE.imagen = imagen
        BE.x = x
        BE.y = y
        BE.texto = texto
        BE.font = font
        BE.text = BE.font.render(BE.texto, True, celeste)
        if imagen is None:
            BE.imagen = BE.text
        BE.rect = BE.imagen.get_rect(center=(BE.x,BE.y))
        BE.text_rect = BE.text.get_rect(center=(BE.x, BE.y))
        
    def update(BE):
        if BE.imagen is not None:
            pantalla.blit(BE.imagen,BE.rect)
        pantalla.blit(BE.text, BE.text_rect)

    def botonApretado(BE, position):
        if position[0] in range(BE.rect.left, BE.rect.right) and position[1] in range(BE.rect.top, BE.rect.bottom):
            return True
        return False

    def cambiarDeColor(BE, posicion):
        if posicion[0] in range(BE.text_rect.left, BE.text_rect.right) and posicion[1] in range(BE.text_rect.top, BE.text_rect.bottom):
            BE.text = BE.font.render(BE.texto, True, plateado)
        else:
            BE.text = BE.font.render(BE.texto, True, celeste)
    
    

humano_surface = pygame.transform.scale(humano,(110,110))

#iconoHumano1 = botonEquipo(humano_surface, 85, 625)
#iconoHumano2 = botonEquipo(humano_surface, 290, 625)
#iconoHumano3 = botonEquipo(humano_surface, 495, 625)
#iconoHumano4 = botonEquipo(humano_surface, 700, 625)
#iconoHumano5 = botonEquipo(humano_surface, 905, 625)
#iconoHumano6 = botonEquipo(humano_surface, 1110, 625)




def obtenerObjeto(id):
    conn = sql.connect("Registro.db")
    cursor = conn.execute("SELECT nombreObjeto FROM objetos where objetoID = ?",
        (id,))
    for row in cursor:
        return(row[0])
    
def obtenerMovimiento(id):
    conn = sql.connect("Registro.db")
    cursor = conn.execute("SELECT nombreMovimiento FROM movimientos where movimientoID = ?",
        (id,))
    for row in cursor:
        return(row[0])
    
#botonOpcion_surface = pygame.transform.scale()

while True:
    #pantalla.fill(azul)
    pantalla.blit(cielo, (0,0))
    #pantalla.blit(edificiosDeFondo, (0,-100))
    #pantalla.blit(jefecitoEnfadadito,(0,-220))
    #pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    #pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    #pygame.draw.rect(pantalla,(celestePastel), (400,200,300,300), width= 100,border_radius=100)
    #mostrarTexto("WENAS",FTimes, celeste, 500,500)
    #mostrarTexto("ÑYA ÑYA ÑYA HAHA",FPapyro, celeste,15,500)
    #mostrarTexto("EEEEEEEEEEEEEEEEEEEEEEEE",FCalacaChida, celeste,35,500)
    #pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    #pygame.display.update()

    #menu de movimientos
    #pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    #pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    #mostrarTexto(obtenerMovimiento(2),FOCRM,celeste, 625, 385)
    #mostrarTexto(obtenerMovimiento(3),FOCRM,celeste, 50, 450)
    #mostrarTexto(obtenerMovimiento(4),FOCRM,celeste, 625, 450)
    #mostrarTexto("<--",FOCRM,(celeste),50,525)
    #mostrarTexto("-->",FOCRM,(celeste),1150,525)


    #menu de objetos
    #pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    #pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    #mostrarTexto(obtenerObjeto(1),FOCRM,celeste, 50, 385)
    #mostrarTexto(obtenerObjeto(5),FOCRM,celeste, 350, 385)
    #mostrarTexto(obtenerObjeto(3),FOCRM,celeste, 650, 385)
    #mostrarTexto(obtenerObjeto(4),FOCRM,celeste, 950, 385)
    #mostrarTexto(obtenerObjeto(6),FOCRM,celeste, 250, 485)
    #mostrarTexto(obtenerObjeto(8),FOCRM,celeste, 750, 485)
    #iconoHumano1.update()
    #iconoHumano2.update()
    #iconoHumano3.update()
    #iconoHumano4.update()
    #iconoHumano5.update()
    #iconoHumano6.update()
    pygame.draw.rect(pantalla,(rosaOscuro),(150, 600, 75,20))
    pygame.draw.rect(pantalla,(rosaOscuro),(355, 600, 75,20))
    pygame.draw.rect(pantalla,(amarillo),(355, 650, 75,20))
    pygame.draw.rect(pantalla,(rosaOscuro),(560, 600, 75,20))
    pygame.draw.rect(pantalla,(amarillo),(560, 650, 75,20))
    pygame.draw.rect(pantalla,(rosaOscuro),(765, 600, 75,20))
    pygame.draw.rect(pantalla,(amarillo),(765, 650, 75,20))
    pygame.draw.rect(pantalla,(rosaOscuro),(970, 600, 75,20))
    pygame.draw.rect(pantalla,(amarillo),(970, 650, 75,20))
    pygame.draw.rect(pantalla,(rosaOscuro),(1175, 600, 75,20))
    pygame.draw.rect(pantalla,(amarillo),(1175, 650, 75,20))


    #mostrarTexto("<-",FOCRM,celestePastel, 250, 400)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()