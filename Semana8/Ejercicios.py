presupuesto = 1000
gasto = 0

while gasto < presupuesto:
    compra = float(input("Monto a comprar: "))
    gasto += compra # forma corta de i = i+1
print("Ha llegado al limite del presupuesto")
print(f"El monto gastado es de {gasto:,.2f}")

#############################

# Herramientas de control de flujo
# Bucle finito: (for), utilizo una coleccion, un string, una lista, una tupla, un diccionario, etc.
palabra = "Hola"
print(len(palabra))
lista = [10, 11, 12, 13, 14]
print(len(lista))
dias = ["Lunes", "Martes", "Miercoles", 
        "Jueves", "Viernes", "Sabado", "Domingo"]
print(len(dias))

for i in dias: # va a repetir segun la cantidad de elementos en la coleccion 
    # i es el iterador
    # lista es el iterable
    print(i) # imprima cada uno de los elementos en mi coleccion


# Auxiliar para crear listas: range(inicio, final) 
# *si pongo un solo valor, lo asume como final
for i in range(5):
    print("Buenos dias")

for i in dias[3]:
    print(i)
# Para imprimir cada uno de los caracteres del cuarto elemento de 'dias' en una linea distinta

valores = [[1,3,6],
           [2,7,4],
           [6,5,9],
           [1,10,20]]
mayores = []
for v in valores:
    for i in v:
        if i>6:
            mayores.append(i)
print(mayores)