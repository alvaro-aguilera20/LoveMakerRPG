#importar librearias, SQLite3 viene con python

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

def crearTablas():
    conn = sql.connect("Registro.db")
    cursor = conn.cursor()
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
    cursor.execute(
        """CREATE TABLE inventarios(
        inventarioID INTEGER PRIMARY KEY,
        lukas FLOAT
        objeto1 INTEGER,
        objeto2 INTEGER,
        objeto3 INTEGER,
        objeto4 INTEGER,
        objeto5 INTEGER,
        objeto6 INTEGER,
        CONSTRAINT FOREIGN KEY(objeto1) REFERENCES objetos(objetoID),
        CONSTRAINT FOREIGN KEY(objeto2) REFERENCES objetos(objetoID),
        CONSTRAINT FOREIGN KEY(objeto3) REFERENCES objetos(objetoID),
        CONSTRAINT FOREIGN KEY(objeto4) REFERENCES objetos(objetoID),
        CONSTRAINT FOREIGN KEY(objeto5) REFERENCES objetos(objetoID),
        CONSTRAINT FOREIGN KEY(objeto6) REFERENCES objetos(objetoID)
        );"""
    )    
    cursor.execute(
        """CREATE TABLE movesets(
        movesetID INTEGER PRIMARY KEY,
        movimiento1 INTEGER,
        movimiento2 INTEGER,
        movimiento3 INTEGER,
        movimiento4 INTEGER,
        movimiento5 INTEGER,
        movimiento6 INTEGER,
        movimiento7 INTEGER,
        movimiento8 INTEGER,
        movimiento9 INTEGER,
        movimiento10 INTEGER,
        CONSTRAINT FOREIGN KEY(movimiento1) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento2) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento3) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento4) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento5) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento6) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento7) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento8) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento9) REFERENCES movimientos(movimientoID),
        CONSTRAINT FOREIGN KEY(movimiento10) REFERENCES movimientos(movimientoID)
        );"""
    )
    cursor.execute(
        """CREATE TABLE Humanos(
            humanoID  INTEGER PRIMARY KEY,
            nombreHumano VARCHAR (50),
            salud FLOAT,
            fuerza  FLOAT,
            mochila INTEGER,
            movimientosHumano INTEGER,
            CONSTRAINT FOREIGN KEY(mochila) REFERENCES inventarios(inventarioID),
            CONSTRAINT FOREIGN KEY(movimientosHumano) REFERENCES movesets(movesetID)
        );"""
    )
    cursor.execute(
        """CREATE TABLE bots(
            botID  INTEGER PRIMARY KEY,
            nombreBOT VARCHAR (50),
            salud FLOAT,
            fuerza  FLOAT,
            energia FLOAT,
            movimientosBot INTEGER,
            CONSTRAINT FOREIGN KEY(movimientosBot) REFERENCES movesets(movesetID)
        );"""
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
   crearTablas()

#al final no pude corregir el error del inventario en adelante, estare viendo eso mañana, esten atentos