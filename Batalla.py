#importar librearias, SQLite3 viene con python


import sqlite3 as sql





#antes recuerden hacer en la terminal el pip instal pygame


import pygame





#con esto inicializamos el proceso de procesar letras


pygame.init()





pygame.font.Font()





#definir graficos que sacamos de la carpeta graficos



nada = pygame.image.load("graficos/Nada.png")

humano1 = pygame.image.load("graficos/Humano1.png")

humano2 = pygame.image.load("graficos/Humano2.png")

humano3 = pygame.image.load("graficos/Humano3.png")


humano4 = pygame.image.load("graficos/Humano4.png")
Bot1 = pygame.image.load("graficos/Bot1.png")

Bot2 = pygame.image.load("graficos/Bot2.png")

Bot3 = pygame.image.load("graficos/Bot3.png")

Bot4 = pygame.image.load("graficos/Bot4.png")

Bella = pygame.image.load("graficos/Bella.png")

Angel = pygame.image.load("graficos/Angel.png")

Glitter = pygame.image.load("graficos/Glitter.png")

Black = pygame.image.load("graficos/Black.png")

Miguel = pygame.image.load("graficos/Miguel.png")

Carlos = pygame.image.load("graficos/Carlos.png")

Shadowfave = pygame.image.load("graficos/Shadowface.png")

MontañitasFondo = pygame.image.load("graficos/montañitas.png")

PasilloFondo = pygame.image.load("graficos/pasilloFondo.png")

SinLuz = pygame.image.load("graficos/FueraDeServicioFondo.png")





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


    
def obtenerNombreObjeto(id):


    conn = sql.connect("Registro.db")



    cursor = conn.execute("SELECT nombreObjeto FROM objetos where objetoID = ?",


        (id,))


    for row in cursor:

        return(row[0])


    


def obtenerNombreMovimiento(id):



    conn = sql.connect("Registro.db")



    cursor = conn.execute("SELECT nombreMovimiento FROM movimientos where movimientoID = ?",

        (id,))

#activar los iconos de los personajes que usaremos mas adelante

    for row in cursor:


        return(row[0])
    
    #automatizacion


def mostrarNombreHumano(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT nombreHumano FROM humanos where humanoID = ?",


        (id,))


    for row in cursor:


        return(row[0])

#definir opciones para el menu de humano

    conn.close()

def obtenerSaludHumano(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT salud FROM humanos where humanoID = ?",


        (id,))


    for row in cursor:


        return(row[0])


    conn.close()

def obtenerFuerzaHumano(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT fuerza FROM humanos where humanoID = ?",


        (id,))


    for row in cursor:


        return(row[0])


    conn.close()

def obtenerSaludBot(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT salud FROM bots where botID = ?",


        (id,))


    for row in cursor:


        return(row[0])


    conn.close()


def obtenerFuerzaBot(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT fuerza FROM bots where botID = ?",


        (id,))


    for row in cursor:


        return(row[0])


    conn.close()

def obtenerEnergiaBot(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT energia FROM bots where botID = ?",


        (id,))


    for row in cursor:


        return(row[0])


    conn.close()

def obtenerCantidadObjetos(id):


    conn = sql.connect("Registro.db")


    cursor = conn.execute("SELECT cantidad FROM objetos where objetoID = ?",


        (id,))


    for row in cursor:


        return(row[0])


fondo1 = pygame.transform.scale(MontañitasFondo,(1280,720))

fondo2 = pygame.transform.scale(CiudadFondo,(1280,720))


pantalla.blit(fondo2,(0,-300))



accederMenuMovimientosPersonaje1 = boton(None, 225, 450,FOCR,"ATACAR")


accederMenuObjetos = boton(None, 875, 450,FOCR,"Objetos")





#funcionamiento del sistema dentro de la maquina

#listar movimientos chico normal, Bella, Angel, Shadowface, Glitter, Black

mov = [[6,7,0,0,0,0,0,0],[1,2,3,4,5,6,7,0],[6,7,8,9,10,11,12,0],[6,19,20,0,0,0,0,0],[13,14,15,16,17,7,0,0],[17,18,20,21,0,0,0,0]]

graficosBotones = [[humano1,humano2,humano3,humano4],[Bot1,Bot2,Bot3]]

graficosOponentes = [[Miguel,Carlos],[Bella, Angel, Glitter]]
#esqueletos bases jugador, oponente

t = [[],
     [],
     []]

o = [[],
     [],
     []]

#diccionarios de equipos

MiguelE = [[1,1],
          [1,3,4,5,6,7],
          [mov[0],mov[1]]]

AngelE = [[2,2],
         [3,0,0,0,0,0],
         [mov[0],mov[2]]]

ShadowFaceE = [[3,3,4],
              [7,10,9,8,0,0],
              [mov[3],mov[4],mov[5]]]

#meter datos solo index

def introducirDatosJugador(jugador):
    t[0]=(jugador[0])
    t[1]=(jugador[1])
    t[2]=(jugador[2])

def introducirDatosOponente(Oponente):
    o[0]=(Oponente[0])
    o[1]=(Oponente[1])
    o[2]=(Oponente[2])

#esqueleto datos del jugador

jugador = [[[],[]],
           #bots / salud, fuerza, energia
           [[],[],[]],
           [[],[],[]],
           [[],[],[]],
           [[],[],[]],
           [[],[],[]],
           #objetos, concretamente su cantidad
           [[],[],[],[],[],[]]]

#esqueleto datos oponente

oponente = [[[],[]],
           #bots / salud, fuerza, energia
           [[],[],[]],
           [[],[],[]],
           [[],[],[]],
           [[],[],[]],
           [[],[],[]],
           #objetos, concretamente su cantidad
           [[],[],[],[],[],[]]]

#insertar datos al esqueleto

introducirDatosJugador(MiguelE)

introducirDatosOponente(AngelE)

#humano salud y fuerza
jugador[0][0] = obtenerSaludHumano(t[0][0])
jugador[0][1] = obtenerFuerzaHumano(t[0][0])
#bot salud, fuerza y energia
for i in range (len(t[0])-1):
    jugador [i+1][0] = obtenerSaludBot(t[0][i+1])
    jugador [i+1][1] = obtenerFuerzaBot(t[0][i+1])
    jugador [i+1][2] = obtenerEnergiaBot(t[0][i+1])

#objeto cantidad

for i in range (6):
    if obtenerCantidadObjetos(t[1][i]) == None:
        jugador [6][i] = 0
    else:
        jugador [6][i] = obtenerCantidadObjetos(t[1][i])

#humano salud y fuerza
oponente[0][0] = obtenerSaludHumano(o[0][0])
oponente[0][1] = obtenerFuerzaHumano(o[0][0])
#bot salud, fuerza y energia
for i in range (len(o[0])-1):
    oponente [i+1][0] = obtenerSaludBot(o[0][i+1])
    oponente [i+1][1] = obtenerFuerzaBot(o[0][i+1])
    oponente [i+1][2] = obtenerEnergiaBot(o[0][i+1])

#objeto cantidad

for i in range (6):
    if obtenerCantidadObjetos(o[1][i]) == None:
        oponente [6][i] = 0
    else:
        oponente [6][i] = obtenerCantidadObjetos(o[1][i])

#definir botones


Objeto1 = boton(None, 125, 425, FOCRM, obtenerNombreObjeto(t[1][0]))


Objeto2 = boton(None, 425, 425, FOCRM, obtenerNombreObjeto(t[1][1]))


Objeto3 = boton(None, 725, 425, FOCRM, obtenerNombreObjeto(t[1][2]))


Objeto4 = boton(None, 1025, 425, FOCRM, obtenerNombreObjeto(t[1][3]))


Objeto5 = boton(None, 450, 500, FOCRM, obtenerNombreObjeto(t[1][4]))


Objeto6 = boton(None, 900, 500, FOCRM, obtenerNombreObjeto(t[1][5]))



def inventario():


    while True:

        Objeto1 = boton(None, 125, 425, FOCRM, obtenerObjeto(1))

iconoHumano1 = boton(pygame.transform.scale(graficosBotones[0][(t[0][0])-1],(110,110)), 85, 625,FOCR,"")

try:
    iconoBot1 = boton(pygame.transform.scale(graficosBotones[1][(t[0][1])-1],(110,110)), 290, 625,FOCR,"")
except IndexError:
    iconoBot1 = boton(pygame.transform.scale(nada,(110,110)), 290, 625,FOCR,"")

try:
    iconoBot2 = boton(pygame.transform.scale(graficosBotones[1][(t[0][2])-1],(110,110)), 495, 625,FOCR,"")
except IndexError:
    iconoBot2 = boton(pygame.transform.scale(nada,(110,110)), 495, 625,FOCR,"")

try:
    iconoBot3 = boton(pygame.transform.scale(graficosBotones[1][(t[0][3])-1],(110,110)), 700, 625,FOCR,"")
except IndexError:
    iconoBot3 = boton(pygame.transform.scale(nada,(110,110)), 700, 625,FOCR,"")

try:
    iconoBot4 = boton(pygame.transform.scale(graficosBotones[1][(t[0][4])],(110,110)), 905, 625,FOCR,"")
except IndexError:
    iconoBot4 = boton(pygame.transform.scale(nada,(110,110)), 905, 625,FOCR,"")


try:
    iconoBot5 = boton(pygame.transform.scale(graficosBotones[1][(t[0][5])-1],(110,110)), 1110, 625,FOCR,"")
except IndexError:
    iconoBot5 = boton(pygame.transform.scale(nada,(110,110)), 1110, 625,FOCR,"")

oponentes = [[pygame.transform.scale(Miguel,(300,300)),pygame.transform.scale(Bella,(300,400))],[pygame.transform.scale(Angel,(500,450)), pygame.transform.scale(Carlos,(150,300))],[]]

oposicion = [[(400,100),(350,0)],[(350,-25), (350,100)],[]]

        Objeto3 = boton(None, 725, 425, FOCRM, obtenerObjeto(4))    


        Objeto4 = boton(None, 1025, 425, FOCRM, obtenerObjeto(6))


        Objeto5 = boton(None, 450, 500, FOCRM, obtenerObjeto(8))    


        Objeto6 = boton(None, 900, 500, FOCRM, obtenerObjeto(9))
        
        
        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        Objeto1.cambiarDeColor(posicionMouse)


        Objeto1.update()


        Objeto2.cambiarDeColor(posicionMouse)


        Objeto2.update()


        Objeto3.cambiarDeColor(posicionMouse)


        Objeto3.update()


        Objeto4.cambiarDeColor(posicionMouse)


        Objeto4.update()


        Objeto5.cambiarDeColor(posicionMouse)


        Objeto5.update()


        Objeto6.cambiarDeColor(posicionMouse)


        Objeto6.update()


        iconoHumano1.update()


        iconoBot1.update()


        iconoBot2.update()


        iconoBot3.update()


        iconoBot4.update()


        iconoBot5.update()


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





        for event in pygame.event.get():


            if event.type == pygame.QUIT:


                pygame.quit()


                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if iconoBot1.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


        pygame.display.update()





def MenuMovimientosHumano1():


    while True:


        movimiento1 = boton(None, 300, 420, FOCRM, obtenerNombreMovimiento(t[2][0][0]))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerNombreMovimiento(t[2][0][1]))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerNombreMovimiento(t[2][0][2]))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerNombreMovimiento(t[2][0][3]))
        
        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        movimiento1.cambiarDeColor(posicionMouse)


        movimiento1.update()


        movimiento2.cambiarDeColor(posicionMouse)


        movimiento2.update()


        movimiento3.cambiarDeColor(posicionMouse)


        movimiento3.update()


        movimiento4.cambiarDeColor(posicionMouse)


        movimiento4.update()


        FlechaI.cambiarDeColor(posicionMouse)


        FlechaI.update()


        FlechaD.cambiarDeColor(posicionMouse)


        FlechaD.update()


        iconoHumano1.update()


        iconoBot1.update()


        iconoBot2.update()


        iconoBot3.update()


        iconoBot4.update()


        iconoBot5.update()


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





        for event in pygame.event.get():


            if event.type == pygame.QUIT:


                pygame.quit()


                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if iconoBot2.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


                if FlechaI.botonApretado(posicionMouse):


                    MenuMovimientosHumano2()


                if FlechaD.botonApretado(posicionMouse):


                    MenuMovimientosHumano2()


        pygame.display.update()





def MenuMovimientosHumano2():

    

    while True:


        movimiento1 = boton(None, 300, 420, FOCRM, obtenerNombreMovimiento(t[2][0][4]))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerNombreMovimiento(t[2][0][5]))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerNombreMovimiento(t[2][0][6]))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerNombreMovimiento(t[2][0][7]))



        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)

        movimiento1.cambiarDeColor(posicionMouse)


        movimiento1.update()


        movimiento2.cambiarDeColor(posicionMouse)


        movimiento2.update()


        movimiento3.cambiarDeColor(posicionMouse)


        movimiento3.update()


        movimiento1.cambiarDeColor(posicionMouse)


        movimiento1.update()


        movimiento2.cambiarDeColor(posicionMouse)


        movimiento2.update()


        movimiento3.cambiarDeColor(posicionMouse)


        movimiento3.update()

        movimiento4.cambiarDeColor(posicionMouse)


        movimiento4.update()

        FlechaI.cambiarDeColor(posicionMouse)


        FlechaI.update()


        FlechaD.cambiarDeColor(posicionMouse)


        FlechaD.update()


        iconoHumano1.update()


        iconoBot1.update()


        iconoBot2.update()


        iconoBot3.update()


        iconoBot4.update()


        iconoBot5.update()


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





        for event in pygame.event.get():


            if event.type == pygame.QUIT:


                pygame.quit()


                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if iconoBot1.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if FlechaI.botonApretado(posicionMouse):


                    MenuMovimientosHumano1()


                if FlechaD.botonApretado(posicionMouse):


                    MenuMovimientosHumano1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


    


        pygame.display.update()








def MenuHumano():


    while True:


        posicionMouse = pygame.mouse.get_pos()

        for i in range (len(o[0])):
            pantalla.blit(oponentes[((o[0][0])-1)][i], oposicion[((o[0][0])-1)][i])


        #pygame.draw.rect(pantalla,(celestePastel), (400,200,300,300), width= 100,border_radius=100)


        botOponente = pygame.transform.scale(Bella,(300,400))


        humanoOponente = pygame.transform.scale(Miguel,(300,300))


        pantalla.blit(humanoOponente,(550,100))


        pantalla.blit(botOponente,(500,0))


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        accederMenuMovimientosPersonaje1.cambiarDeColor(posicionMouse)


        accederMenuMovimientosPersonaje1.update()


        accederMenuObjetos.cambiarDeColor(posicionMouse)


        accederMenuObjetos.update()


        iconoHumano1.update()


        iconoBot1.update()


        iconoBot2.update()


        iconoBot3.update()


        iconoBot4.update()


        iconoBot5.update()


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





        for event in pygame.event.get():


            if event.type == pygame.QUIT:


                pygame.quit()


                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if accederMenuMovimientosPersonaje1.botonApretado(posicionMouse):


                    MenuMovimientosHumano1()


                if iconoBot2.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if accederMenuObjetos.botonApretado(posicionMouse):


                    inventario()


                if iconoBot1.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


        pygame.display.update()

def MenuMovimientosBot1_1():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerNombreMovimiento(t[2][1][0]))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerNombreMovimiento(t[2][1][1]))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerNombreMovimiento(t[2][1][2]))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerNombreMovimiento(t[2][1][3]))

        



        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        movimiento1.cambiarDeColor(posicionMouse)


        movimiento1.update()


        movimiento2.cambiarDeColor(posicionMouse)


        movimiento2.update()


        movimiento3.cambiarDeColor(posicionMouse)


        movimiento3.update()


        movimiento4.cambiarDeColor(posicionMouse)


        movimiento4.update()


        FlechaI.cambiarDeColor(posicionMouse)


        FlechaI.update()


        FlechaD.cambiarDeColor(posicionMouse)


        FlechaD.update()


        iconoHumano1.update()


        iconoBot1.update()


        iconoBot2.update()


        iconoBot3.update()


        iconoBot4.update()


        iconoBot5.update()


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





        for event in pygame.event.get():


            if event.type == pygame.QUIT:


                pygame.quit()


                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if iconoBot2.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


                if FlechaI.botonApretado(posicionMouse):


                    MenuMovimientosBot1_2()


                if FlechaD.botonApretado(posicionMouse):


                    MenuMovimientosBot1_2()


        pygame.display.update()

def MenuMovimientosBot1_2():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerNombreMovimiento(t[2][1][4]))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerNombreMovimiento(t[2][1][5]))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerNombreMovimiento(t[2][1][6]))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerNombreMovimiento(t[2][1][7]))


        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        movimiento1.cambiarDeColor(posicionMouse)


        movimiento1.update()


        movimiento2.cambiarDeColor(posicionMouse)


        movimiento2.update()


        movimiento3.cambiarDeColor(posicionMouse)


        movimiento3.update()


        movimiento4.cambiarDeColor(posicionMouse)


        movimiento4.update()


        FlechaI.cambiarDeColor(posicionMouse)


        FlechaI.update()


        FlechaD.cambiarDeColor(posicionMouse)


        FlechaD.update()


        iconoHumano1.update()


        iconoBot1.update()


        iconoBot2.update()


        iconoBot3.update()


        iconoBot4.update()


        iconoBot5.update()


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





        for event in pygame.event.get():


            if event.type == pygame.QUIT:


                pygame.quit()


                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:


                if iconoBot2.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


                if FlechaI.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


                if FlechaD.botonApretado(posicionMouse):


                    MenuMovimientosBot1_1()


        pygame.display.update()


MenuHumano()