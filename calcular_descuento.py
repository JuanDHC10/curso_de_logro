producto = int(input("Ingrese el precio del producto: "))
descuento = int(input("Ingrese el descuento del producto: "))

producto_descuento = producto / descuento
menor = producto_descuento < 100

print("Descuento aplicado al producto: ", producto_descuento)
print("El precio final es menor a 100:", menor)