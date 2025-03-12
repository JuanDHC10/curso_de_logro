estudiantes = int(input("Cuantos estudiantes hay en la clase: "))

calificaciones = [] 

print("")

for i in range(estudiantes):
    calificacion = int(input(f"Ingrese la calificacion del estudiante {i + 1}: "))
    calificaciones.append(calificacion) 

print("")

suma_calificacion = sum(calificaciones) 
print(f"La suma de las calificaciones es: ", suma_calificacion)

suma_promedio = suma_calificacion / estudiantes
print(f"El promedio es: ", suma_promedio)

calificacion_alta = max(calificaciones)
print(f"La calificacion mas alta es: ", calificacion_alta)

calificacion_baja = min(calificaciones)
print(f"La calificacion mas baja es: ", calificacion_baja)

print("")