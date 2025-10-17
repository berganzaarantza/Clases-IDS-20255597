#Se introduce correo
correo = input()

#Condición 1: un @
cantidad_arrobas = correo.count("@")
cantidad_valida = (cantidad_arrobas==1)

#Condición 2: antes y despues de @ hay al menos tres caracteres
posicion = correo.index("@")
posicion_inicio = correo[0:posicion]


#Condición 3: al menos un punto
cantidad_punto = correo.count(".")
validez_punto = (cantidad_punto>=1)

#Condición 4: no espacios
cantidad_espacios = correo.count(" ")
validez_espacios = (cantidad_espacios<=0)

#Condición 5: no inicia ni termina con punto
punto_no_inicio = (correo[0]!=".")
punto_no_final = (correo[-1]!=".")

print(cantidad_valida,validez_punto,validez_espacios,punto_no_inicio,punto_no_final)