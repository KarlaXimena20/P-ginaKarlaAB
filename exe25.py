name=input("Ingresa tu primer nombre: ")
if len(name)<5:
    n=input("Ingresa tu apellido")
    word= name + n
    print(word.upper())
else:
    print(name.lower())