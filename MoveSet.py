def MenuMovimientos1():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(2))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))



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

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(1))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))



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

def MenuMovimientos3():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(2))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))



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

def MenuMovimientos4():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(2))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))



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

def MenuMovimientos5():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(1))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))



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

def MenuMovimientos6():


    while True:

        movimiento1 = boton(None, 300, 420, FOCRM, obtenerMovimiento(2))


        movimiento2 = boton(None, 900, 420, FOCRM, obtenerMovimiento(3))


        movimiento3 = boton(None, 300, 480, FOCRM, obtenerMovimiento(5))


        movimiento4 = boton(None, 900, 480, FOCRM, obtenerMovimiento(6))



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

