import os
from usuarios import usuario
from usuarios import usuario as model
class accion():
    def registro(self):
            nombre = input("cual es tu nombre\n")
            os.system("cls")
            apellidos = input("cual es tu apellido\n")
            os.system("cls")
            email = input("cual es tu email\n")
            os.system("cls")
            password = input("cual es tu contrasena \n")
            os.system("cls")
            user = model.usuario(nombre,apellidos,email,password)
            regis = user.registrar()
            if regis[0]>= 1:
                 print(f"\nregistro creado por {regis[1].nombre}, con el correo {regis[1].correo}")
            else :
                 print("el registro no se ha podido crear")
    
    def login(self):      
        print("=======bienvenido al login-----------\n")
        email = input("cual es tu email\n")
        os.system("cls")
        password = input("cual es tu contrasena \n")
        os.system("cls")