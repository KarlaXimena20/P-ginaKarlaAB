print("1) Cuadrado")
print("2) Triángulo")
print()
ms=int(input("Ingrese un número: "))
if ms == 1:
    lado=int(input("Ingrese la longitud de uno de los lados: "))
    area=lado*lado
    print("El área de la figura seleccionada es: ", area)
elif ms == 2:
    base=int(input("Ingrese el largo de la base: "))
    altura=int(input("Ingrese la altura del triángulo: "))
    area=(base*altura)/2
    print("El área de la figura seleccionada es: ", area)
else:
    print("Seleccionaste una opción incorrecta")