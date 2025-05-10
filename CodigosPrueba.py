import sqlite3 as sql






import pygame





pygame.init()





pygame.font.Font()





#definir graficos que sacamos de la carpeta graficos


cielo = pygame.image.load("graficos/cielo.png")


edificiosDeFondo = pygame.image.load("graficos/edificios.png")


humano1 = pygame.image.load("graficos/humano1.png")


Bot1 = pygame.image.load("graficos/Bot1.png")


Bella = pygame.image.load("graficos/Bella.png")


Miguel = pygame.image.load("graficos/Miguel.png")





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





pantalla.blit(cielo, (0,0))


pantalla.blit(edificiosDeFondo, (0,-100))





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


    


humano_surface = pygame.transform.scale(humano1,(110,110))


bot1_surface = pygame.transform.scale(Bot1,(110,110))





iconoHumano1 = boton(humano_surface, 85, 625,FOCR,"")


iconoBot1 = boton(bot1_surface, 290, 625,FOCR,"")


iconoBot2 = boton(bot1_surface, 495, 625,FOCR,"")


iconoBot3 = boton(bot1_surface, 700, 625,FOCR,"")


iconoBot4 = boton(bot1_surface, 905, 625,FOCR,"")


iconoBot5 = boton(bot1_surface, 1110, 625,FOCR,"")





accederMenuMovimientosPersonaje1 = boton(None, 225, 450,FOCR,"ATACAR")


accederMenuObjetos = boton(None, 875, 450,FOCR,"Objetos")





Objeto1 = boton(None, 125, 425, FOCRM, obtenerObjeto(1))


Objeto2 = boton(None, 425, 425, FOCRM, obtenerObjeto(3))


Objeto3 = boton(None, 725, 425, FOCRM, obtenerObjeto(4))


Objeto4 = boton(None, 1025, 425, FOCRM, obtenerObjeto(6))


Objeto5 = boton(None, 450, 500, FOCRM, obtenerObjeto(8))


Objeto6 = boton(None, 900, 500, FOCRM, obtenerObjeto(9))





movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(2))


movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))


movimiento5 = boton(None, 900, 480, FOCRM, obtenerMovimiento(7))


FlechaI = boton(None, 75, 525,FOCRM, "<--")


FlechaD = boton(None, 1200, 525,FOCRM, "-->")





def inventario():


    while True:


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


                    MenuMovimientos1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


        pygame.display.update()





def MenuMovimientos1():


    while True:





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


                    MenuMovimientos2()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


                if FlechaI.botonApretado(posicionMouse):


                    MenuMovimientos2()


                if FlechaD.botonApretado(posicionMouse):


                    MenuMovimientos2()


        pygame.display.update()





def MenuMovimientos2():


    while True:





        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        movimiento5.cambiarDeColor(posicionMouse)


        movimiento5.update()


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


                    MenuMovimientos1()


                if FlechaI.botonApretado(posicionMouse):


                    MenuMovimientos1()


                if FlechaD.botonApretado(posicionMouse):


                    MenuMovimientos1()


                if iconoHumano1.botonApretado(posicionMouse):


                    MenuHumano()


    


        pygame.display.update()








def MenuHumano():


    while True:


        posicionMouse = pygame.mouse.get_pos()


        pygame.draw.rect(pantalla,(negro), (0,360,1280,360),border_top_left_radius=25,border_top_right_radius=25)


        pygame.draw.rect(pantalla,(azul), (0,360,1280,360), width= 25,border_radius=25)


        #pygame.draw.rect(pantalla,(celestePastel), (400,200,300,300), width= 100,border_radius=100)


        botOponente = pygame.transform.scale(Bella,(300,400))


        humanoOponente = pygame.transform.scale(Miguel,(300,300))


        pantalla.blit(humanoOponente,(400,100))


        pantalla.blit(botOponente,(350,0))


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


                    MenuMovimientos1()


                if iconoBot2.botonApretado(posicionMouse):


                    MenuMovimientos2()


                if accederMenuObjetos.botonApretado(posicionMouse):


                    inventario()


                if iconoBot1.botonApretado(posicionMouse):


                    MenuMovimientos1()


        pygame.display.update()





MenuHumano()