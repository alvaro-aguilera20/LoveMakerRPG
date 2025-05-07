#importar librearias, SQLite3 viene con python
import sqlite3 as sql

#antes recuerden hacer en la terminal el pip instal pygame
import pygame

#con esto inicializamos el proceso de procesar letras
pygame.init()

pygame.font.Font()

#definir graficos que sacamos de la carpeta graficos

humano = pygame.image.load("graficos/Humano.png")
waffle = pygame.image.load("graficos/Bot1.png")
mandy = pygame.image.load("graficos/bot2.png")

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
amarillo = (253,253,150)

#resolucion de la pantalla
pantalla=pygame.display.set_mode((1280,720))
pygame.display.set_caption("ventana basica")

#definir fuentes de texto

FArial = pygame.font.SysFont("Arial", 100)
FTimes = pygame.font.SysFont("times",12)
FPapyro = pygame.font.SysFont("Papyrus", 12)
FCalacaChida = pygame.font.SysFont("comic sans", 12)
FOCR = pygame.font.SysFont("OCR A EXTENDED",100)
FOCRM = pygame.font.SysFont("OCR A EXTENDED",50)
#definir mostrar texto (necesita el texto que quieres meter, la fuente ya definida, el color definido o no, y las coordenadas X e Y)

def mostrarTexto(texto, fuente, color, X, Y):
    Text= fuente.render(texto, True, color)
    pantalla.blit(Text,(X,Y))

#definir iconos del equipo

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
bot1_surface = pygame.transform.scale(waffle,(110,110))
bot2_surface = pygame.transform.scale(mandy,(110,110))

iconoHumano1 = boton(humano_surface, 85, 625,FOCR,"")
iconoBot1 = boton(bot1_surface, 290, 625,FOCR,"")
iconoBot2 = boton(bot2_surface, 495, 625,FOCR,"")
iconoHumano4 = boton(humano_surface, 700, 625,FOCR,"")
iconoHumano5 = boton(humano_surface, 905, 625,FOCR,"")
iconoHumano6 = boton(humano_surface, 1110, 625,FOCR,"")

accederMenuMovimientosPersonaje1 = boton(None, 225, 450,FOCR,"ATACAR")
accederMenuObjetos = boton(None, 875, 450,FOCR,"Objetos")
#definir busqueda por base de datos

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

#con este comando la pantalla seguira abierta hasta que la cerremnos manualmente o se acabe el juego
while True:
    posicionMouse = pygame.mouse.get_pos()

    pantalla.fill(negro)
    mandyOponente = pygame.transform.scale(mandy,(600,400))
    pantalla.blit(mandyOponente,(350,0))
    pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)
    pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)
    accederMenuMovimientosPersonaje1.cambiarDeColor(posicionMouse)
    accederMenuMovimientosPersonaje1.update()
    accederMenuObjetos.cambiarDeColor(posicionMouse)
    accederMenuObjetos.update()
    iconoHumano1.update()
    iconoBot1.update()
    iconoBot2.update()
    iconoHumano4.update()
    iconoHumano5.update()
    iconoHumano6.update()
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

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()