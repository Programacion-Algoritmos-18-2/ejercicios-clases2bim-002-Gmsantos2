import codecs # importamos los modulos a utilizar, para la lectura del archivo
import sys

class MiArchivo: #clase
    """
    """
    
    def __init__(self): #metodo init para la inicializacion de las variables globales
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r") #a la variable le mandamos la informacion de la direccion del archivo

    def obtener_informacion(self): # metodo donde retornamos la variable con  todos los datos del archivo
        return self.archivo.readlines() 

    def cerrar_archivo(self): #metodo para cerrar el archivo 
        self.archivo.close()


class MiArchivoEscribir: #metodo para modificar el archivo en caso de estar vacio
    """
    """
    
    def __init__(self): #init donde esta la variable global
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a") #a la variable le mandamos la informacion de la direccion del archivo

    def agregar_informacion(self, p): #metodo donde recibe un objeto y reescribe el archivo
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo)) 

    def cerrar_archivo(self): #metodo cerrar archivo
        self.archivo.close()
