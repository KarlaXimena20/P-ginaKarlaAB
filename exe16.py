raining=input("¿Está lloviendo?")
raining=str.lower(raining)
if raining == "yes":
    windy=input("¿Hay mucho viento?")
    windy=str.lower(windy)
    if windy == "yes":
        print("Hay mucho viento como para llevar una sombrilla")
    else:
            print("Lleva una sombrilla")
else:
    print("Disfruta tu día")