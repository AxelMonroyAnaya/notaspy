from conexion import conexion
import datetime
conectar = conexion.conexion()
cursor = conectar.cursor()
cursor.execute("select * FROM usuarios")
print(cursor.fetchall())
print(conectar)

class usuario():
    def __init__(self,nombre, apellidos, email, passwd):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email 
        self.passwd = passwd
    
    @property
    def getNom(self):
        return self.nombre
    @property
    def getAp(self):
        return self.apellidos
    @property
    def getEma(self):
        return self.email
    
    def setnombre(self, nuevonombre):
        self.nombre = nuevonombre 

    def setAp(self, nuevoApe):
        self.apellidos = nuevoApe

    def setEma(self, nuevoEmail):
        self.email = nuevoEmail 

    def setContra(self, nuevaContra):
        self.passwd = nuevaContra
    
    def registrar(self ):
        fecha = datetime.datetime.now()
        url ="INSERT INTO usuarios VALUES(null, %s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, self.passwd, fecha)
        cursor.execute(url, usuario)
        conectar.commit()
        return [cursor.rowcount, self]

    
    
    

