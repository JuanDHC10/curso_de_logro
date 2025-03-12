presentacion = "Bienvenido al juego de Escapa Rapido"
presentacion_mejor = presentacion.upper()
print(presentacion_mejor)

print("")
# Tu estado en el laberinto
print("Te encuentras en un laberinto y necesitas salir rapido de alli debes tomar buenas decisiones para salir con vida, sino soltaran los perros de caza come humanos y te destrozaran")

print("")
# Caminos para la salida
print("Te encuentras desesperado, sudado, con ganas de salir y despues de 3 dias sin comer en el laberinto, estas debilitado y con poca fuerza, decides avanzar sin rendirte en busca de la salida, pero sabes que no sera facil salir, despues de 20 minutos caminando vez 1 camino, el camino es muy oscuro y silencioso")

print("")
# Objetos del cofre
objeto1 = "linterna"
objeto2 = "Encendedor"
linterna = objeto1.upper()
encendedor = objeto2.upper()

# objetos del cadaver
objeto3 = "soga"
objeto4 = "escalera"
objeto5 = "pipa"
soga = objeto3.upper()
escalera = objeto4.upper()
pipa = objeto5.upper()

# opciones para la salida
salida1 = "bajar rapido"
salida2 = "bajar lento"
bajarra = salida1.upper()
bajarle = salida2.upper()

# Primera toma de decision
print(f"Al mirar a la derecha hay un cofre en el cofre hay solo 3 objetos que te ayudaran a salir debes tomar una buena decision.")
print(f"En el cofre hay: ", "1:", linterna, "2:", encendedor)

print("")

eleccion1 = input("Cual de estos objetos eliges: ")

print("")

if eleccion1 == "linterna":
    print(f"Tomas la", linterna ,"y caminas lentamente para la salida, al alumbrar las paredes de alrededor vez diferentes animales como: arañas, tuqueques, garrapatas, insectos, etc. Comienzas a ver un poco de luz y te apresuras, al llegar vez un tapon pero al mirar arriba esta la luz del sol y tu opcion es subir arriba")
    
    print("")

    print("hay un cadaver que tiene 3 objetos para subir ese muro, debes elegir el correcto, ya falta poco para que suelten a los perros. Date prisa")

    print("")

    print(f"Estos son los objetos que tiene el cadaver a su alrededor: ", "1:", soga, "2:", escalera)

    eleccion2 = input("Cual de estos objetos eliges para subir el muro: ")

    print("")

    if eleccion2 == "soga":
        print("Vez la cabeza del cadaver y esta agrietado en la cabeza, la soga esta guindada arriba del muro en un tuvo y sospechas que la persona(el cadaver) intento subir y se cayo. Subes y vez la luz del sol despues de 3 dias, te estiras, respiras y te relajas 5 minutos, a tu derecha hay una bajada(tipo como un cerro), pero sabes que al bajar esta la salida")

        print("puedes bajar corriendo con miedo a que te caigas, por lo inclinado que esta o puedes bajar lento y salir con mas cuidado pero ojo ya estan tras de ti los perros y debes tomar la mejor decision")

        print("")

        print("Estas son tus opciones: ", bajarra, "o", bajarle)

        eleccion3 = input("Que prefieres: ")

        if eleccion3 == "bajar rapido":
            print("Te arriesgaste y en medio de la bajada al correr te caiste pero te hiciste una leve raspada pero lograste salir, felicidades")

        elif eleccion3 == "bajar lento":
            print("Decides ir despacio, pero ya los perros logran localizarte, debes de ser un poco mas rapido, por poco casi te deboran, pero lograste salir, Felicidades")
        else:
            print("No has seleccionado correctamente o no escribiste bien el objeto a elegir")

        print("")

    elif eleccion2 == "escalera":
        print("Tomas la", escalera, "procedes a ponerla en el sitio correcto para subir el muro, al subir vez depues de 3 dias y te alegras de ver la luz del sol, te das prisa para salir y vez una bajadita(un cerro) y es la opcion de salida, debes tomar una decision.")

        print("puedes bajar corriendo con miedo a que te caigas, por lo inclinado que esta o puedes bajar lento y salir con mas cuidado pero ojo ya estan tras de ti los perros y debes tomar la mejor decision")

        print("")

        print("Estas son tus opciones: ", bajarra, "o", bajarle)

        eleccion3 = input("Que prefieres: ")

        if eleccion3 == "bajar rapido":
            print("Te arriesgaste y en medio de la bajada al correr te caiste pero te hiciste una leve raspada pero lograste salir, felicidades")

        elif eleccion3 == "bajar lento":
            print("Decides ir despacio, pero ya los perros logran localizarte, debes de ser un poco mas rapido, por poco casi te deboran, pero lograste salir, Felicidades")

        else:
            print("No has seleccionado correctamente o no escribiste bien el objeto a elegir")

    else:
        print("No has seleccionado correctamente o no escribiste bien el objeto a elegir")


elif eleccion1 == "encendedor":
    print(f"Tomas el", encendedor , "y no se te hace facil ver, pero decides seguir avanzando con cuidado ya que no observas bien donde pisas, Comienzas a ver un poco de luz y te apresuras, al llegar vez un tapon pero al mirar arriba esta la luz del sol y tu opcion es subir arriba")

    print("")

    print("hay un cadaver que tiene 3 objetos para subir ese muro, debes elegir el correcto, ya falta poco para que suelten a los perros. Date prisa")

    print("")

    print(f"Estos son los objetos que tiene el cadaver a su alrededor: ", "1:", soga, "2:", escalera)

    eleccion2 = input("Cual de estos objetos eliges para subir el muro: ")

    if eleccion2 == "soga":
        print("Vez la cabeza del cadaver y esta agrietado en la cabeza, la soga esta guindada arriba del muro en un tuvo y sospechas que la persona(el cadaver) intento subir y se cayo. Subes y vez la luz del sol despues de 3 dias, te estiras, respiras y te relajas 5 minutos, a tu derecha hay una bajada(tipo como un cerro), pero sabes que al bajar esta la salida")

        print("puedes bajar corriendo con miedo a que te caigas, por lo inclinado que esta o puedes bajar lento y salir con mas cuidado pero ojo ya estan tras de ti los perros y debes tomar la mejor decision")

        print("")

        print("Estas son tus opciones: ", bajarra, "o", bajarle)

        eleccion3 = input("Que prefieres: ")

        print("")

        if eleccion3 == "bajar rapido":
            print("Te arriesgaste y en medio de la bajada al correr te caiste pero te hiciste una leve raspada pero lograste salir, felicidades")

        elif eleccion3 == "bajar lento":
            print("Decides ir despacio, pero ya los perros logran localizarte, debes de ser un poco mas rapido, por poco casi te deboran, pero lograste salir, Felicidades")
        else:
            print("No has seleccionado correctamente o no escribiste bien el objeto a elegir")

        print("")

    elif eleccion2 == "escalera":
        print("Tomas la", escalera, "procedes a ponerla en el sitio correcto para subir el muro, al subir vez depues de 3 dias y te alegras de ver la luz del sol, te das prisa para salir y vez una bajadita(un cerro) y es la opcion de salida, debes tomar una decision.")

        print("puedes bajar corriendo con miedo a que te caigas, por lo inclinado que esta o puedes bajar lento y salir con mas cuidado pero ojo ya estan tras de ti los perros y debes tomar la mejor decision")

        print("")

        print("Estas son tus opciones: ", bajarra, "o", bajarle)

        eleccion3 = input("Que prefieres: ")

        print("")

        if eleccion3 == "bajar rapido":
            print("Te arriesgaste y en medio de la bajada al correr te caiste pero te hiciste una leve raspada pero lograste salir, felicidades")

        elif eleccion3 == "bajar lento":
            print("Decides ir despacio, pero ya los perros logran localizarte, debes de ser un poco mas rapido, por poco casi te deboran, pero lograste salir, Felicidades")

    else:
        print("No has seleccionado correctamente o no escribiste bien el objeto a elegir")

else:
    print("No has seleccionado correctamente o no escribiste bien el objeto a elegir")