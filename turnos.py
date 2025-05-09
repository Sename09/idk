import random
ganar = False
seguir = True
turno = 1
puntos1 = 0
puntos2 = 0
punto_turno = 0
while ganar == False:
    if ganar == False:
        print (f"***es el turno del jugador {turno}: ")
        seguir = True
    while seguir == True:
        if turno == 1:
            seguir = int(input("¿quieres lanzar el dado?\n si(1)\t no(2) : "))
            if seguir == 1:
                seguir = True
                punto_turno = random.randint(1,6)
                if punto_turno != 1:
                    puntos1 = puntos1 + punto_turno
                    print (f"salio un {punto_turno}\ntus puntos son : {puntos1}")
                    if puntos1 >= 10:
                        ganar = True
                        seguir = False
                else:
                    puntos1 = 0
                    print (f"salio un {punto_turno}\ntus puntos son : {puntos1}")
                    turno = 2
                    seguir = False
            else:
                seguir = False
                turno = 2
        else:
            seguir = int(input("¿quieres lanzar el dado?\nsi(1)\t no(2) : "))
            if seguir == 1:
                seguir = True
                punto_turno = random.randint(1,6)
                if punto_turno != 1:
                    puntos2 = puntos2 + punto_turno
                    print(f"salio un {punto_turno}\ntus puntos son : {puntos2}")
                    if puntos2 >= 10:
                        ganar = True
                        seguir = False
                else:
                    puntos2 = 0
                    (f"salio un {punto_turno}\ntus puntos son : {puntos2}")
                    turno = 1
                    seguir = False
            else:
                turno = 1
                seguir = False
print ("fin")