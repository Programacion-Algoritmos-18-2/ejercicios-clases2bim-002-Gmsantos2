"""
    creación de clases
"""

class Persona(object): #clase persona
    """
    """
    
    def __init__(self, n, ape, ed, cod,n1,n2): #init con las variables de la clase
        """
        """
        self.nombre = n   #inicializacion de variables
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    #METODOS AGREGAR Y OBTENER
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self,n):
        self.nota1 = n

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota2(self,n):
        self.nota2 = n

    def obtener_nota2(self):
        return self.nota2

    
    #metodo toString
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.obtener_nombre(), self.obtener_apellido(),\
                self.obtener_edad(), self.obtener_codigo(), self.obtener_nota1(), self.obtener_nota2())


class OperacionesPersona(object): #clase operaciones 
    """
    """
    
    def __init__(self, listado): #init  con las variables globales
        """
        """
        self.listado_personas = listado
        


    def obtener_promedio_1(self): #metodo para obtener el promedio de las notas 1
        suma = 0
        for n in self.listado_personas: #for que recorre la lista  que recibe como parametro
            suma = suma + n.obtener_nota1() #se van sumando los valores
        promedio_1 = suma / len(self.listado_personas) #el promedio que divide a la suma para el tamanio de la lista
        return promedio_1 #retorna el promedio

    def obtener_promedio_2(self): #metodo para obtener el promedio de las notas 2
        suma = 0
        for n in self.listado_personas: #for que recorre la lista  que recibe como parametro
            suma = suma + n.obtener_nota2()#se van sumando los valores
        promedio_2 = suma / len(self.listado_personas) #el promedio que divide a la suma para el tamanio de la lista
        return promedio_2 #retorna el promedio 2


    def obtener_listado_n1(self): #metodo para obtener el listaso de notas 1
        cadena = ""
        for n in self.listado_personas:  #for que recorre la lista  que recibe como parametro
            if (n.obtener_nota1() < 15): #codicional que entra cuando la nota es menor a 15
                cadena = "%s\n%s %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena #retorna la cadena con los nombres

    def obtener_listado_n2(self):
        cadena = ""
        for n in self.listado_personas:  #for que recorre la lista  que recibe como parametro
            if (n.obtener_nota2() < 15):#codicional que entra cuando la nota es menor a 15
                cadena = "%s\n%s %s\n " % (cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena #retorna la cadena con los nombres

    def obtener_listado_personas(self, a , b): #metodo listado de personas que recibe 2  string
        cadena = ""
        
        for n in self.listado_personas: #for que recorre la lista  que recibe como parametro
            if (a==n.obtener_nombre()[0] or b==n.obtener_nombre()[0]): #if que compara  los valores  que  llegan con la inicial , posicion[0]
                cadena = "%s\n%s %s\n " % (cadena, n.obtener_nombre(), n.obtener_apellido())
        return cadena


    #metodo toString
    def __str__(self): 
        """
        """
        cadena = ""
        for n in self.listado_personas: #for que recorre la lista  que recibe como parametro
            cadena = "%s\n%s %s" %(cadena, n.obtener_nombre(), n.obtener_apellido())

        return cadena #retorna la cadena



