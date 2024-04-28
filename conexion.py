import mysql.connector
def conexion():
    global Conex
    Conex = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "proyectoMaster",
        port = 3308
        
     )
    return Conex




