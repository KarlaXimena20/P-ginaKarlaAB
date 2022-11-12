name=input("Ingresa tu nombre: ")
num=int(input("Ingresa un número: "))
if num < 10:
    for i in range(0,num):
        print(name)
    else:
        for i in range(0,3):
            print("Muy alto")