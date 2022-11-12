total=0
for i in range(0,5):
    num=int(input("Inserte un número: "))
    ans=input("¿Desea incluir este número? Si o No")
    if ans == "Si":
        total= total + num
        print(total)