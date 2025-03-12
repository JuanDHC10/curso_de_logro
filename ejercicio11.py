edad = int(input("Ingrese su edad: "))

resultado = edad >= 18 and edad <= 65

resultado2 = not(edad) <= 18 

print(f"La persona tiene entre 18 y 65 años: ", resultado)
print(f"La persona es mayor de edad: ", resultado2)