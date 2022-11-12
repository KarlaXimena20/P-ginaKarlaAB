num1=int(input("Ingrese un número: "))
total= num1
again= "y"
while again == "y":
    num2=int(input("Ingrese otro número: "))
    total= total + num2
    again=input("¿Deseas ingresar otro número? (s/n)")
    print("El total es: ", total)
