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



#metodo para crear base de datos
#def crearBD():
#    conn = sql.connect("Registro.db")
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#    crearBD()

#fin del metodo, si quieren hacerlo en casa quiten los hashtags

#creacion de tablas

#def crearTablas():
#    conn = sql.connect("Registro.db")
#    cursor = conn.cursor()
    #cursor.execute(
    #    """CREATE TABLE objetos(
    #    objetoID INTEGER PRIMARY KEY,
    #    nombreObjeto VARCHAR (20),
     #   potenciador FLOAT,
      #  descripcionObjeto VARCHAR (100)
      #  )"""
    #)
    #cursor.execute(
#        """CREATE TABLE movimientos(
 #       movimientoID INTEGER PRIMARY KEY,
  #      nombremovimiento VARCHAR (20),
   #     daño FLOAT,
    #    terreno INTEGER,
     #   costo  FLOAT,
      #  descripcionMovimiento VARCHAR (100)
       # );"""
#    )
#    cursor.execute(
#        """CREATE TABLE inventarios(
#        inventarioID INTEGER PRIMARY KEY,
#        lukas FLOAT
#        objeto1 INTEGER,
#        objeto2 INTEGER,
#        objeto3 INTEGER,
#        objeto4 INTEGER,
#        objeto5 INTEGER,
#        objeto6 INTEGER,
#        FOREIGN KEY(objeto1) REFERENCES objetos(objetoID),
#        FOREIGN KEY(objeto2) REFERENCES objetos(objetoID),
#        FOREIGN KEY(objeto3) REFERENCES objetos(objetoID),
#        FOREIGN KEY(objeto4) REFERENCES objetos(objetoID),
#        FOREIGN KEY(objeto5) REFERENCES objetos(objetoID),
#        FOREIGN KEY(objeto6) REFERENCES objetos(objetoID)
#        );"""
#    )    
#    cursor.execute(
#        """CREATE TABLE movesets(
#        movesetID INTEGER PRIMARY KEY,
#        movimiento1 INTEGER,
#        movimiento2 INTEGER,
#        movimiento3 INTEGER,
#        movimiento4 INTEGER,
#        movimiento5 INTEGER,
#        movimiento6 INTEGER,
#        movimiento7 INTEGER,
#        movimiento8 INTEGER,
#        movimiento9 INTEGER,
#        movimiento10 INTEGER,
#        FOREIGN KEY(movimiento1) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento2) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento3) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento4) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento5) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento6) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento7) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento8) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento9) REFERENCES movimientos(movimientoID),
#        FOREIGN KEY(movimiento10) REFERENCES movimientos(movimientoID)
#        );"""
#    )
#    cursor.execute(
#        """CREATE TABLE Humanos(
#            humanoID  INTEGER PRIMARY KEY,
#            nombreHumano VARCHAR (50),
#            salud FLOAT,
#            fuerza  FLOAT,
#            mochila INTEGER,
#            movimientosHumano INTEGER,
#            FOREIGN KEY(mochila) REFERENCES inventarios(inventarioID),
#            FOREIGN KEY(movimientosHumano) REFERENCES movesets(movesetID)
#        );"""
#    )
#    cursor.execute(
#        """CREATE TABLE bots(
#            botID  INTEGER PRIMARY KEY,
#            nombreBOT VARCHAR (50),
#            salud FLOAT,
#            fuerza  FLOAT,
#            energia FLOAT,
#            movimientosBot INTEGER,
#            FOREIGN KEY(movimientosBot) REFERENCES movesets(movesetID)
#        );"""
#    )
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#   crearTablas()

#al final no pude corregir el error del inventario en adelante, estare viendo eso mañana, esten atentos