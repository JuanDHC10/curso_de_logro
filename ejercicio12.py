calificacion = int(input("Ingrese su calificacion: "))

if calificacion >= 90 and calificacion <= 100:
    print("Su rango es: A")
elif calificacion >= 80 and calificacion <= 89:
    print("Su rango es: B")
elif calificacion >= 70 and calificacion <= 79:
    print("Su rango es: C")
elif calificacion >= 60 and calificacion <= 69:
    print("Su rango es: D")
else:
    print("Su rango es: F")