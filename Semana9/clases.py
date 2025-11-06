# Vamos a crear un Diccionario
mi_gato = {
    "nombre" : "pelusa", 
    "edad" : 3, 
    "caracteristica" : "simpatico"
}
camis_cat = {
    "caracteristica" : "simpatico",
    "nombre" : "pelusa",
    "edad" : 3
}
print(len(mi_gato))
print(mi_gato)
print(camis_cat)

copia = mi_gato == camis_cat
print(copia)


birthdays = {
    "Alice" : "Abr 1",
    "Bob" : "Dic 12",
    "Carol" : "Mar 4",
}

print(birthdays["Bob"])

birthdays["Carol"] = "Abr 21" # Para modificar un valor
print(birthdays["Carol"])

birthdays["Fer"] = "Mar 3" # Para agregar un valor
print(birthdays)

for persona, fecha in birthdays.items():
    print(f"El cumpleaños de {persona} es en {fecha}")

del birthdays ["Bob"] # Para borrar (delete) un valor
print(birthdays)


# A un diccionario vacio le voy agregando datos
semana = {}
semana["uno"] = "lunes"
semana["dos"] = "martes"
semana["tres"] = "miercoles"
semana["cuatro"] = "jueves"
semana["cinco"] = "viernes"
print(semana)

for anona in semana.values(): # Este .valor me genera una secuencia con los valores
    print(anona) # lunes

for anona in semana.keys(): 
    print(anona) # uno

for anona, uva in semana.items(): # Un iterable de pares, uno de claves y uno de valores
    print(f"El dia {anona} de la semana es {uva}.") # El dia uno de la semana es lunes.


# Solo toma en cuenta los valores que no estan repetidos
colores = {"rojo", "rojo", "verde", "negro", "azul"}
print(type(colores))
print(len(colores))
print(colores)

surnames = ["Rivest", "Shamir", "Adleman"]
for position, surname in enumerate(surnames):
    print(position,surnames)

surnames = ["Rivest", "Shamir", "Adleman"]
for position, surname in enumerate(surnames, start = 1): # Comienza en 1 y no en 0
    print(position,surnames)

people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]
for person, age in zip(people, ages):
    print(person,age)

people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]
instruments = ["Drums", "Keyboards", "Bass", "Guitar"]
for person in instruments:
    print(person,instruments)


