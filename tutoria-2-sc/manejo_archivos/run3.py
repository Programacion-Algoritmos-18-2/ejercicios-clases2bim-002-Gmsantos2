from paquete_archivos.miarchivo import MiArchivo  #importacion de los paquetes donde estan las clases a utilizar
from paquete_modelo.mimodelo import Persona , OperacionesPersona

m = MiArchivo() #inicializamos a m  con
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]


# print(lista)

lista = lista[1:]
lista_personas = [] #inicializacion de una lista vacia
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
    # print(d)
    #suman1 = suman1 + int(d[4])    
    p = Persona(d[1], d[2], d[3], d[0], d[4],d[5]) # inicializamos el objeto p con  el objeto persona y le mandamos los valores de lista en tal posicion 
    lista_personas.append(p) #lista vacia le agregamos el objeto con los valores
    
    
operaciones = OperacionesPersona(lista_personas)# objet operaciones inicializada con  la clase ue recibe una lista

print(operaciones) #imprimimos el objeto  operaciones
print("PROMEDIO 1 ") #encabezado
print(operaciones.obtener_promedio_1()) #imprimimos el objeto  operaciones (en este caso el metodo obtener promedio 1) RETORNA una cadena
print("PROMEDIO 2")#encabezado
print(operaciones.obtener_promedio_2()) #imprimimos el objeto  operaciones (en este caso el metodo obtener promedio 2)RETORNA una cadena
print("LISTADO NOTAS 1")#encabezado
print(operaciones.obtener_listado_n1()) #imprimimos el objeto  operaciones (el listado de nombres de notas 1 menores que 15)
print("LISTADO NOTAS 2")#encabezado
print(operaciones.obtener_listado_n2())#imprimimos el objeto  operaciones (el listado de nombres de notas 2 menores que 15)
print("LISTADO INICIALES R Y J")#encabezado
print(operaciones.obtener_listado_personas("R", "J")) #imprimimos el objeto operaciones (listado de las personas que inician su nombre con R y J)