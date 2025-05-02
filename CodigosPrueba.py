import sqlite3 as sql

import pygame

conn = sql.connect

def mostrarObjeto(id):
    return conn.execute("SELECT nombreObjeto FROM objetos WHERE objetoID == {id}")

print (mostrarObjeto(2))

pygame.init()

pygame.font.Font()

#definir graficos que sacamos de la carpeta graficos
cielo = pygame.image.load("graficos/cielo.png")
edificiosDeFondo = pygame.image.load("graficos/edificios.png")
jefecitoEnfadadito = pygame.image.load("graficos/jefe.png")

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

pantalla=pygame.display.set_mode((1280,720))
pygame.display.set_caption("ventana basica")

FArial = pygame.font.SysFont("Arial", 50)
FTimes = pygame.font.SysFont("times",100)
FPapyro = pygame.font.SysFont("Papyrus", 50)
FCalacaChida = pygame.font.SysFont("comic sans", 50)
Flucida = pygame.font.SysFont("lucida sans typewritter",100)
FOCR = pygame.font.SysFont("OCR A EXTENDED",100)

def mostrarTexto(texto, fuente, color, X, Y):
    Text= fuente.render(texto, True, color)
    pantalla.blit(Text,(X,Y))

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
    #mostrarTexto("PATADA",FOCR,celeste, 50, 400)
    #mostrarTexto("MOV2",FOCR,celeste, 650, 400)
    #mostrarTexto("MOV3",FOCR,celeste, 50, 550)
    #mostrarTexto("MOV4",FOCR,celeste, 650, 550)
    #mostrarTexto("<-",FOCR,celestePastel, 400, 400)

    #menu de objetos
    pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    mostrarTexto("OBJ1",FOCR,celeste, 50, 400)
    #mostrarTexto("OBJ2",FOCR,celeste, 650, 400)
    #mostrarTexto("OBJ3",FOCR,celeste, 50, 550)
    #mostrarTexto("OBJ4",FOCR,celeste, 650, 550)
    #mostrarTexto("<-",FOCR,celestePastel, 400, 400)
    pygame.display.update()

    #menu de equipo
    #pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    #pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    #mostrarTexto("TU",FOCR,celeste, 50, 400)
    #mostrarTexto("BOT",FOCR,celeste, 650, 400)
    #mostrarTexto("<-",FOCR,celestePastel, 400, 400)
    #pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()