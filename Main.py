import sqlite3 as sql

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
#    cursor.execute(
#        """CREATE TABLE objetos(
#        objetoID INTEGER PRIMARY KEY,
#        nombreObjeto VARCHAR (20),
#        efecto VARCHAR(2),
#        factor FLOAT,
#        cantidad INTEGER,
#        descripcionObjeto VARCHAR (100)
#        )"""
#    )
#    cursor.execute(
#        """CREATE TABLE movimientos(
#        movimientoID INTEGER PRIMARY KEY,
#        nombremovimiento VARCHAR (20),
#        daño FLOAT,
#        efecto VARCHAR(2),
#        terreno INTEGER,
#        costo  FLOAT,
#        descripcionMovimiento VARCHAR (100)
#        );"""
#    )
#    cursor.execute(
#        """CREATE TABLE Humanos(
#            humanoID  INTEGER PRIMARY KEY,
#            nombreHumano VARCHAR (50),
#            salud FLOAT,
#            fuerza  FLOAT,
#            lukas FLOAT
#        );"""
#    )
#    cursor.execute(
#        """CREATE TABLE bots(
#            botID  INTEGER PRIMARY KEY,
#            nombreBOT VARCHAR (50),
#            salud FLOAT,
#            fuerza  FLOAT,
#            energia FLOAT
#        );"""
#    )
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#   crearTablas()

#al final no pude corregir el error del inventario en adelante, estare viendo eso mañana, esten atentos

#insertar personajes, en este caso insertamos a miguel, carlos y shadowface, junto a sus respectivos bots

#def meterDatosDeHumanos():
#    conn = sql.connect("Registro.db")
#    conn.execute("""INSERT INTO Humanos(nombreHumano, salud, fuerza, lukas) \
#                 VALUES ("Miguel", 40.0 , 2.0, 20.0),
#                        ("carlos", 30.0, 3.0, 10.0),
#                        ("ShadowFace", 80.0 , 5.0, 500.0)
#    """)
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#    meterDatosDeHumanos()

#insertar algunos objetos y movimientos

#def verHumanos():
#    conn = sql.connect("Registro.db")
#    cursor = conn.execute("SELECT * FROM Humanos")
#    for row in cursor:
#        print("ID ", row[0])
#        print("Nombre ", row[1])
#        print("Salud ", row[2])
#        print("Fuerza ", row[3])
#        print("Lukas $", row[4], "\n")
#    conn.close()

#if __name__ == "__main__":
#    verHumanos()

#insertar bots

#def meterDatosDeBots():
#    conn = sql.connect("Registro.db")
#    conn.execute("""INSERT INTO bots(nombreBot, salud, fuerza, energia) \
#                 VALUES ("Bella", 30.0 , 3.0, 200.0),
#                        ("Angel", 70.0, 7.0, 77.0),
#                        ("Glitter", 100.0 , 5.0, 100.0),
#                        ("Black", 65.0 , 4.0, 50.0)
#    """)
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#    meterDatosDeBots()

#def verBots():
#    conn = sql.connect("Registro.db")
#    cursor = conn.execute("SELECT * FROM bots")
#    for row in cursor:
#        print("ID ", row[0])
#        print("Nombre ", row[1])
#        print("Salud ", row[2])
#        print("Fuerza ", row[3])
#        print("Energia ", row[4], "\n")
#    conn.close()

#if __name__ == "__main__":
#    verBots()

#def meterDatosDeObjetos():
#    conn = sql.connect("Registro.db")
#    conn.execute("""INSERT INTO objetos(nombreObjeto, efecto, factor, cantidad, descripcionObjeto) \
#                 VALUES ("Fierro", "+", 2, 1, "en lugar de golpear con los puños pega con este fierro de imitacion"),
#                        ("Fierro golpeador de parejas felices", "+", 100, 1, "causa inmenso daño a las parejas felices pero te hace inutil contra personas que van solas"),
#                        ("medkit", "+", 50, 5, "curas 50 de salud al humano si le han hecho daño (NO FUNCIONA EN BOTS)"),
#                        ("bateria", "+", 50, 6, "recarga 50 puntos de energia si el bot la ha gastado"),
#                        ("navaja", "*", 2, 1, "duplica el daño que haces"),
#                        ("pistola", "-", 50, 6, "dispara para quitarle un monton de salud a tu rival"),
#                        ("cable transformador", "/", 2, 3, "roba la mitad de energia que tenga el oponente y la transforma hacia tu bot"),
#                        ("bate", "+", 4, 1, "suma 4 a tu daño"),
#                        ("rifle", "-", 50, 30, "rifle de asalto"),
#                       ("soldador portatil", "+", 50, 8, "repara la salud de tu bot si ha sufrido daño")
#    """)
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#    meterDatosDeObjetos()

#def verObjetos():
#    conn = sql.connect("Registro.db")
#    cursor = conn.execute("SELECT * FROM objetos")
#    for row in cursor:
#        print("ID ", row[0])
#        print("como se llama la wea", row[1])
#        print("que hace ", row[2])
#        print("cuanta potencia tiene ", row[3])
#        print("cuanto dura ", row[4])
#        print("Descripcion detallada: ", row[5], "\n")
#    conn.close()

#if __name__ == "__main__":
#    verObjetos()

#metemos ahora los movimientos

#def meterDatosDeMovimientos():
#    conn = sql.connect("Registro.db")
#    conn.execute("""INSERT INTO movimientos(nombremovimiento, daño, efecto, terreno, costo, descripcionMovimiento) \
#                 VALUES ("parguas protector", 0, "-", 0, 10, "protege a quien haya escogido para ese turno"),
#                        ("nube", 1, "+", 1, 5, "invoca una nube que cambia el terreno, si invoca mas con el territorio ya cambiado el terreno se vera afectado hasta llegar a la etapa final donde hay nieve"),
#                        ("rayo", 80, "-", 0, 50,"un poderoso rayo que hace mucho daño, en tormentas electricas sale gratis sin necedidad de gastar energia"),
#                        ("baja de temperatura", 10, "-", 5, 15,"hace que la temperatura baje bestialmente hasta estar como el polo norte, esto hace los humanos se muevan mas lento que los bots"),
#                        ("estocada", 5, "*", 0 , 0, "ataque preciso que puede ser usado solo cuando un bot trae un arma larga cuerpo a cuepro"),
#                        ("patada", 4, "*", 0, 0, "una poderosa patada, tan podersa que te quita 2 de salud"),
#                        ("puñetazo", 2, "*", 0, 0, "un simple puñetazo, intenta darle bien al objetivo xd"),
#                        ("bendicion vida eterna", 1, "+", 0, 50, "hace inmune a todo al objetivo al bendecirle, funciona solo mientras el usuario este vivo"),
#                        ("espada de luz", 7, "*", 0, 7, "equipa al usuario con un poderoso sable de luz el cual multiplica la fuerza que tiene"),
#                        ("volar", 20, "-", 0, 10, "el usuario vuela por los cielos haciendo asi esquivar TODO ataque que no sea de area, este esquive solo es activo por el turno que fue usado, y cuando vuelva a tierra dañara a su objetivo quitandole 20 de salud"),
#                        ("apartados", 0, "", 7, 10, "este terreno niega TODO efecto secundario para todos e impide el uso de objetos o ataque que usen energia y causen daño mayor a 10"),
#                        ("bendicion de salud", 0, "+", 0, 5, "recupera 50 de salud al objetivo si ha sido dañado"),
#                        ("cañon luminoso", 200, "-", 0, 100, "lanza un poderoso rayo luminoso que destroza a lo que toque, pero gasta un monton de energia"),
#                        ("bola disco", 0, "", 6, 20, "activa el terreno de baile, y esto hace que la energia se recarge sola, 10 de energia por turno"),
#                        ("baile", 0, "", 0, 5, "este movimiento hace que todo ataque se dirija directo a ella, pero a su vez reduce el daño a la mitad, el movmiento no consumira energia si esta en el terreno de baile"),
#                        ("purpurina", 5, "-", 0, 2, "resta salud a todos en el campo de batalla y cambia sus objetivos a uno aleatorio"),
#                        ("absorbsion de luz", 50, "+",0 , 0, "recarga la energia del bot, si esta en un terreno que le de luz"),
#                        ("invisibilidad", 0,"+",0 , 10, "vuelve invisible al usuario, solo ataques de area podran dañarlo, sera invisible hasta que use un movmiento que haga daño"),
#                        ("arrebatar",10, "-",0 , 5, "quita al objetivo lo que sea que se haya equipado y lo agrega a si mismo"),
#                        ("robar", 0 ,"-", 0, 10, "apunta al humano y podras robar un objeto de su inventario"),
#                        ("cañon sombra", 50, "-", 0, 40, "un cañon poderoso que suele ocultar en sus brazos, lo dispara cuando creas oportuno"),
#                        ("navaja oculta", 5, "*", 0, 10, "saca un filo y lo añade al brazo para dar mas daño"),
#                        ("purificacion", 0, "+", 0, 5, "devuelve el terreno por defecto a la partida")
#    """)
#    conn.commit()
#    conn.close()

#if __name__ == "__main__":
#    meterDatosDeMovimientos()

#def verMovimientos():
#    conn = sql.connect("Registro.db")
#    cursor = conn.execute("SELECT * FROM movimientos")
#    for row in cursor:
#        print("ID ", row[0])
#        print("como se llama la wea", row[1])
#        print("cuanta potencia tiene ", row[2])
#        print("que hace ", row[3])
#        print("cambio de terreno ", row[4])
#        print("cuanta energia cuesta ", row[5])
#        print("descripcion detallada: ", row[6], "\n")
#    conn.close()

#if __name__ == "__main__":
#    verMovimientos()

conn = sql.connect("Registro.db")

def mostrarObjeto():
    cursor = conn.execute("SELECT nombreObjeto FROM objetos")
    for row in cursor:
        print (row[0])

mostrarObjeto()