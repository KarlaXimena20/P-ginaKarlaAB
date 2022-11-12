num=int(input("¿A cuántos amigos deseas invitar a la fiesta?"))
if num < 10:
    for i in range(0,num):
        name=input("Ingresa un nombre: ")
        print(name, "llegó")
    else:
        print("Son demasiadas personas")