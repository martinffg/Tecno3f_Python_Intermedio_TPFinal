##  Tecno3f - # Python Intermedio - TP Final

# Alumno: Martín F. Fernández Gamen
# Mail: martinffg@gmail.com

## Modo de uso del programa:   

Para correr el programa, basado en el entorno donde fue creado (testeado sobre Windows11) se necesita tener en el equipo instalado 
\# Python 3.13.2 o superior
\# pip 25.1.1 o superior
\# No se utilizan librerías externas: requirements.txt (vacío)

Luego una vez situado en la raíz del proyecto / carpeta del venv correr:

> py main.py

Esto abrirá la ventana del programa de CRUD sobre la DDBB peliculas.db integrada al proyecto.

# Backup de la DB y tablas en csv
Se encuentran dentro de la carpeta ddbb/Backup_DB y ddbb/Backup_tables

## Creando venv y requeriments.txt en Windows:
> py -m venv Test_Entorno           -> creo el venv
> .\Test_Entorno\Scripts\activate   -> activo el venv
> pip freeze > requeriments.txt     -> exporto los paquetes instalados por pip en el venv, para el caso es vacio al no sumar librerías externas.

# FIN
