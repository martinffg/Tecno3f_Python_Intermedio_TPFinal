from .coneciondb import Conneccion


def crear_tabla():
    conn = Conneccion()

    sqlContinente = """
        CREATE TABLE IF NOT EXISTS Continente (
	        Id INTEGER NOT NULL,
	        Nombre TEXT,
	        PRIMARY KEY(Id AUTOINCREMENT)
        );
    """
    sqlPais = """
        CREATE TABLE IF NOT EXISTS Pais (
	        Id INTEGER NOT NULL,
	        Nombre TEXT,
	        Continente INTEGER,
	        PRIMARY KEY(Id AUTOINCREMENT),
	        FOREIGN KEY(Continente) REFERENCES Continente(Id)
        );
    """
    sqlDirector = """
        CREATE TABLE IF NOT EXISTS Director (
	        Id INTEGER NOT NULL,
	        Nombre TEXT,
	        Pais INTEGER,
	        PRIMARY KEY(Id AUTOINCREMENT),
	        FOREIGN KEY(Pais) REFERENCES Pais(Id)
        );
    """

    sqlEstudio = """
        CREATE TABLE IF NOT EXISTS Estudio (
	        Id INTEGER NOT NULL,
	        Nombre TEXT,
	        Pais INTEGER,
	        PRIMARY KEY(Id AUTOINCREMENT),
	        FOREIGN KEY(Pais) REFERENCES Pais(Id)
        );
    """
    sqlGenero = """
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );
    """
    sqlPeliculas = """
        CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL,
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            AnioEstreno VARCHAR(4),
	        Director INTEGER,
	        Estudio INTEGER,
	        Pais INTEGER,
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY(Director) REFERENCES Director(Id),
	        FOREIGN KEY(Estudio) REFERENCES Estudio(Id),
	        FOREIGN KEY(Genero) REFERENCES Genero(ID),
	        FOREIGN KEY(Pais) REFERENCES Pais(Id)
            );
    """

    try:
        conn = Conneccion()
        conn.cursor.execute(sqlContinente)
        conn.cursor.execute(sqlPais)
        conn.cursor.execute(sqlDirector)
        conn.cursor.execute(sqlEstudio)
        conn.cursor.execute(sqlGenero)
        conn.cursor.execute(sqlPeliculas)
        conn.cerrar_con()
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


class Peliculas:

    def __init__(self, nombre, duracion, genero, anioEstreno, director, estudio, pais):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.anioEstreno = anioEstreno
        self.director = director
        self.estudio = estudio
        self.pais = pais

    def __str__(self):
        return f"Pelicula[{self.nombre},{self.duracion},{self.genero},{self.anioEstreno},{self.director},{self.estudio},{self.pais}]"


def guardar_peli(pelicula):
    conn = Conneccion()

    sql = f"""
        INSERT INTO Peliculas(Nombre,Duracion,Genero,AnioEstreno,Director,Estudio,Pais)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero},'{pelicula.anioEstreno}',{pelicula.director},{pelicula.estudio},{pelicula.pais});
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def listar_peli():
    conn = Conneccion()
    listar_peliculas = []

    sql = f"""
        SELECT p.ID,p.Nombre,p.Duracion, g.Nombre Genero , p.AnioEstreno, d.Nombre Director, e.Nombre Estudio, pa.Nombre Pais 
        FROM Peliculas as p
            INNER JOIN Genero as g ON p.Genero = g.ID
            INNER JOIN Director as d ON p.Director = d.ID 
            INNER JOIN Estudio as e ON p.Estudio = e.ID 
            INNER JOIN Pais as pa ON p.Pais = pa.ID;
"""
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()
        # print(listar_peliculas)
        return listar_peliculas
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql = f"""
        SELECT * FROM Genero;
"""
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def listar_directores():
    conn = Conneccion()
    listar_director = []

    sql = f"""
        SELECT * FROM Director;
"""
    try:
        conn.cursor.execute(sql)
        listar_director = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_director
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def listar_estudios():
    conn = Conneccion()
    listar_estudio = []

    sql = f"""
        SELECT * FROM Estudio;
"""
    try:
        conn.cursor.execute(sql)
        listar_estudio = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_estudio
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def listar_paises():
    conn = Conneccion()
    listar_pais = []

    sql = f"""
        SELECT * FROM Pais;
"""
    try:
        conn.cursor.execute(sql)
        listar_pais = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_pais
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def editar_peli(pelicula, id):
    conn = Conneccion()

    sql = f"""
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Genero = {pelicula.genero}, AnioEstreno = '{pelicula.anioEstreno}', Director = {pelicula.director}, Estudio = {pelicula.estudio}, Pais = {pelicula.pais}
        WHERE ID = {id}
        ;
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")


def borrar_peli(id):
    conn = Conneccion()

    sql = f"""
        DELETE FROM Peliculas
        WHERE ID = {id}
        ;
"""
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Ha ocurrido un error. {e}")
