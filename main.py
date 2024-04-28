"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""
import mysql.connector
from conexion import conexion
from usuariosp import acciones
import os


conectar = conexion()
cursor = conectar.cursor()
print(conectar)
os.system("cls")
while True:
    seleccionUser = input("Bienvenido\n selecciona una opcion\n   -REGISTRAR\n   -LOGEAR\n")
    if seleccionUser.upper() in ['REGISTRAR', 'LOGEAR']:
        break
    else:
        os.system("cls")
        print("\ntienes que tipear la opcion que deseas\n")
accion = acciones.accion()
if seleccionUser.upper() == "REGISTRAR":
    accion.registro()
elif seleccionUser.upper() =="LOGEAR":
    accion.login()






