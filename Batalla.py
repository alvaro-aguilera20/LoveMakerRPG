#importar librearias, SQLite3 viene con python
import sqlite3 as sql

#antes recuerden hacer en la terminal el pip instal pygame
import pygame

#con esto inicializamos el proceso de procesar letras
pygame.init()

pygame.font.Font()

#definir graficos que sacamos de la carpeta graficos

#definir los colores que usaremos
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

#resolucion de la pantalla
pantalla=pygame.display.set_mode((1280,720))
pygame.display.set_caption("ventana basica")

#definir fuentes de texto

FArial = pygame.font.SysFont("Arial", 100)
FTimes = pygame.font.SysFont("times",12)
FPapyro = pygame.font.SysFont("Papyrus", 12)
FCalacaChida = pygame.font.SysFont("comic sans", 12)
FOCR = pygame.font.SysFont("OCR A EXTENDED",100)
#definir mostrar texto (necesita el texto que quieres meter, la fuente ya definida, el color definido o no, y las coordenadas X e Y)

def mostrarTexto(texto, fuente, color, X, Y):
    Text= fuente.render(texto, True, color)
    pantalla.blit(Text,(X,Y))


#con este comando la pantalla seguira abierta hasta que la cerremnos manualmente o se acabe el juego
while True:
    pantalla.fill(negro)
    pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    mostrarTexto("ATACAR",FOCR,celeste, 200, 400)
    mostrarTexto("OBJETOS",FOCR,celeste, 700, 400)
    mostrarTexto("EQUIPO",FOCR,celeste, 500, 550)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()