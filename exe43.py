direccion=input("¿Desea contar hacia arriba o hacia abajo? (u/d)")
if direccion == "u":
    num=int(input("¿Cuál es el número más alto? "))
    for i in range(1,num+1):
        print(i)
elif direccion == "d":
        num=int(input("Ingresa un número menor que 20: "))
        for i in range(20,num-1,-1):
            print(i)
        else:
            print("No entiendo")

