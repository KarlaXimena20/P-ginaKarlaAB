cnum=50
guess=int(input("¿Puedes adivinar el número en el que estoy pensando? "))
count=1
while guess != cnum:
    if guess < cnum:
        print("Muy bajo")
    else:
        print("Muy alto")
        count=count + 1
        guess=int(input("Intentálo de nuevo: "))
        print("Bien hecho, tomaste", count, "intentos" )
