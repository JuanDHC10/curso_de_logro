print("Bienvenido al carrito de compra")
print('1: "Si" para entrar')
print('2: "No" para no entrar')
entrada = input("Pon el numero de su eleccion: ")

cesta = []

print("")

while entrada == "si":
    print("1: Agregar un nuevo producto a la cesta")
    print("2: Mostrar los producto que contiene la cesta")
    print("3: Eliminar un producto de la cesta")
    print("4: Calcular los producto de la cesta")
    print("5: salir de la cesta")

    print("")

    eleccion = int(input("Ingrese su opcion poniendo el numero que le corresponde: "))

    print("")

    if eleccion == 1:     
        def añadir_elemento():
            producto = input("Ingrese el producto que desea añadir: ")
            precio = float(input("Ingrese el precio del producto: "))
            if cesta != producto:
                cesta.append(producto)
                cesta.append(precio)
                print(f"{producto} a sido añadido al carrito y su precio es {precio} $")
                print("")
            else:
                print("lo sentimos pero a tenido un error escribiendo su producto o ha puesto algo que no se le ha pedido.")
        añadir_elemento()

    elif eleccion == 2:
        def mostrar_elemetos():
            print("")
            for i in cesta:
                print(i)
        mostrar_elemetos()

    if eleccion == 3:
        def eliminar_elemento():
            print("")
            eliminar = input("Que producto desea eliminar del carrito: ")
            for i in cesta:
                if i == eliminar:
                    cesta.remove(i)
                    print(f"El elemento {i} ha sido eliminado de la cesta")
        eliminar_elemento()

    elif eleccion == 4:
        def calcular():
            suma = sum(cesta)
            print(suma)

    elif eleccion == 5:
        print("")
        print("Que tenga un feliz dia y vuelva pronto!")
        break
    else:
        print("No ha introducido un numero para las opciones o has puesto un numero que no esta como opcion.")
    pass