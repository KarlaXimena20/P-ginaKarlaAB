again="y"
count=0
while again == "y":
    name=input("Ingresa el nombre de alguien que quieres invitar a tu fiesta: ")
    print(name, "ha sido invitado")
    count=count + 1
    again=input("¿Deseas invitar a alguien más? (s/n)")
    print("Tienes", count, "invitados")
