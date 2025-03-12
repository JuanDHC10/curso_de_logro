num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

resultado = num > 0 and num2 > 0

resultado2 = num > 0 or num2 > 0

resultado3 = not(num) > 0

print("Ambos numeros son positivos: ", resultado)
print("Por lo menos uno de los numeros es positivos: ", resultado2)
print("El primer numero es negativo: ", resultado3)