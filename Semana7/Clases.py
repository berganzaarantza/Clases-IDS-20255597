# Trabajando con listas
# Son mutables, puedo cambiar el largo de la lista, reducirlo, etc. La lista es un objeto.
# Tiene propiedades y metodos

datos = [1,2,"tres",["lunes","martes","miercoles"]]
print(datos[2][1]) # Para extraer el segundo valor del dato en la posicion 2, la r de tres
print(len(datos)) # La tupla [] solo cuenta como un elemento
print(datos[3][2][3]) # El ultimo elemento de datos, el ultimo elemento de dias y el tercer valor de miercoles, la r
print(datos[-1][-1][4]) # El ultimo elemento de datos, el ultimo elemento de dias y el cuarto valor de miercoles, la c

###################################

numeros = ["uno","dos","tres"]
print(numeros)

numeros = numeros + ["cuatro","cinco","seis"]
print(len(numeros))
numeros[2]="trois"
print(numeros)

numeros.append(input("Escribe el siguiente numero: ")) # 'append' significa "agregar al final"
print(numeros)

numeros.insert(2,"one") # insert es insertar en una posicion especifica. Utiliza dos valores. En la posicion 2 agrego la palabra "one"
print(numeros)

numeros.insert(2,input("Einender nummer: ")) # En el indice 2, ponga este valor
print(numeros)

###################################

nombre = "Antonio"
repetidos = nombre.lower().count("a")
print(repetidos)

nombres = ["Ana","Antonio","Ana","Jose"]
r_a = 0
print(nombres.count("Maria"))
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)

int(nombres.index("Ana",nombres.index("Ana")+1))

# Agregar a la collecion 'nombres' un elemento al final
nombres = ["Ana","Antonio","Ana",]
print(nombres.append("Abi"))
print(nombres)

# Agregar a la collecion 'nombres' en una posicion especifica
nombres = ["Ana","Antonio","Ana","Jose","Andrea"]
print(nombres)
nombres.insert(2,"Emi")
print(nombres)

#####################

nombres = ["Ana","Antonio","Ana","Jose","Andrea"]
print(nombres.append("Abi"))
print(nombres)
nombres.insert(int(input("Posicion sustituir: ")), input("Nombre nuevo: "))
print(nombres)
posicion = int(input("Posicion sustituir: "))
nombres[posicion] = input("Nombre Nuevo sustituir: ")
print(nombres)
nombres.remove("Andrea")

######################

#Pop modifica la coleccion pero ester valor se puede guardar en otra variable
nombres = ["Ana","Antonio","Ana","Jose","Andrea"]
print(nombres.append("Abi"))
print(nombres)
nombres.insert(int(input("Posicion sustituir: ")), input("Nombre nuevo: "))
print(nombres)
nombre_borrado = nombres.pop(3)
print(f"Nombre borrado: {nombre_borrado}")
print(nombres)

########################

numero = 6

captura = int(input("Adivina el numero (un intento): "))

if captura == numero:
    print("Adivinaste, reina!")
else:
    print("Ella jura que adivinó <3")
print("Sigue jugando, diva")

######################

nota = int(input("Digite la nota: "))

if nota > 8:
    print("You ateee, girl")
elif nota > 6:
    print("Very good, diva")
elif nota > 4:
    print("Study more...")
else:
    print("Lock in, pls")

#####################

# Anidado
monto = float(input("Digite el monto: "))
tipo = input("Tipo (local/internacional): ")
impuesto = 0

if tipo.lower() == "local":
    if monto > 100:
        impuesto = 0.07
    else:
        if monto > 75:
            impuesto = 0.05
        else:
            impuesto = 0

elif tipo.lower() == "internacional": # Si el usuario no digitara "local", suponga evaluar internacional
    if monto > 100:
        impuesto = 0.12
    else:
        if monto > 75:
            impuesto = 0.09
        else:
            impuesto = 0
else:
    print("Ese tipo no existe")

print(f"El tipo {tipo} con monto {monto:,.2f}") # Recomendable imprimir hasta el final
print(f"paga un impuesto de {monto*impuesto:,.2f}")

###########################

nombres = ["Ana","José","Luis"]

for x in nombres: # for Hará algo por cada iterador que encuentre
    print("Hola")

for i in nombres: # i Hace un recorrido
    print(i)

for i in nombres:
    if i == "Jose":
        print("Lo encontre")
    else:
        print("No está José")