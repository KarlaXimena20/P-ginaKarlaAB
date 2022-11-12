import math
radio=int(input("Ingrese el radio del círculo: "))
profundidad:int(input("Ingrese su profundidad: "))
area=math.pi*(radio**2)
volumen=area*profundidad
print(round(volumen, 3))