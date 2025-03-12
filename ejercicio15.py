nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su pais: ")
pelicula = input("Ingrese su pelicula favorita: ")


mi_diccionario = {"nombre": nombre, "apellido": apellido,"edad": edad, "pais": pais, "pelicula favorita": pelicula}

print("")

print("Esta es su informacion recopilada: ")

print("")

print(mi_diccionario["nombre"])
print(mi_diccionario["apellido"])
print(mi_diccionario["edad"])
print(mi_diccionario["pais"])
print(mi_diccionario["pelicula favorita"])

print("")