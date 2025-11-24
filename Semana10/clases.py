#Definimos la funcion
def describir_mascota(tipo_animal: str, nombre_mascota: str):
    """Esta funcion describe una mascota"""
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un tipo de animal {tipo_animal.lower()}")

#Llamamos la funcion
describir_mascota(nombre_mascota="perro", tipo_animal="phoenix")
describir_mascota("gato", "misifus")


#El valor por defecto es perro, y se asume este a menos que el usuario lo defina
def describir_mascota(nombre_mascota:str, tipo_animal:str ="perro"):
    """Esta funcion describe una mascota, por defecto = perro"""
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un tipo de animal {tipo_animal.lower()}")

describir_mascota("misifus", "gato") #Aqui defino que sera un gato


def registro_usuarios(nombre,apellido,inicial):
    """Construir un nombre a partir de sus componentes"""
    nombre_completo = f"{nombre} {inicial} {apellido}"
    return nombre_completo

print(registro_usuarios("Daniel", "Wisecarver", "L")) #Se espera que se pongan tres valores


def registro_usuarios(nombre,apellido,inicial="", edad=0):
    """Construir un nombre a partir de sus componentes"""
    nombre_completo = f"La persona {nombre} {inicial} {apellido} de {edad} años"
    return nombre_completo

print(registro_usuarios("Daniel", "Wisecarver", "L")) #Si no hay un valor en la edad, se define como 0


def registro_usuarios(nombre,apellido,inicial="", edad=0):
    """Construir un nombre a partir de sus componentes"""
    if edad:
        texto_completo = f"La persona {nombre} {inicial} {apellido}, de {edad} años"
    else:
        texto_completo = f"La persona {nombre} {inicial} {apellido}"
    return texto_completo

print(registro_usuarios("Daniel", "Wisecarver")) #Edad no trae un valor por defecto, por lo tanto, produzcalo


#Definimos una funcion que es usada por una lista

def saludar_usuarios(nombres):
    """Saludara al usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")

usuarios = ["ana", "luis", "juan"]
saludar_usuarios(usuarios)


#Vamos a proceder a atender pedidos de pizza

#Definiendo la funcion
def ordenar_pizza(ingrediente1, ingrediente2):
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza de: ") 
    print(f"{ingrediente1}")
    print(f"{ingrediente2}")

#Llamando a la funcion
ordenar_pizza("jamon","tocino")


#Ahora con args
def ordenar_pizza(size,masa,*ingredientes): #Reconoce a los ingredientes como una lista
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de masa {masa} de: ") 
    for i in ingredientes:
        print(f"\t- {i}") #La t la reconoce como una tabulacion

#Llamando a la funcion
ordenar_pizza("grande", "alta", "queso","jamon","pepperoni","tomate","piña") #Size va a tomar el valor de "grande", por ser el primer valor y no entrar en la categoria args


# Vamos a crear una funcion usando kwags para programacion orientada a objetos
"*args es para crear listas"
"**kwargs es para crear diccionarios"

def registro_profesores(nombre,apellido,**materias): #Kwargs sera el ultimo para evitar confusiones
    """Crear un registro de profesor, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items(): #Hago un recorrido por diccionarios
        print(f"\t - {ciclo}: \t {materias}")

registro_profesores(
    "Alvin",
    "Portillo",
    Ciclo1= ["BD1, IIJ","AG&D"],
    Ciclo2= ["DAI","BD2","SINE"],
    Ciclo3= ["IDS", "FPEN", "PAD"]
)