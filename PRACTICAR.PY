nombre1 = input ("Nombre del jugador 1 : ")
print (nombre1.lower())
nombre2 = input ("Nombre del jugador 2 : ")
print (nombre2.lower())

ronda = 1
puesto1 = 0
puesto2 = 0




while ronda <=3:
    print ("RONDA")



    jugador1 = input("¿Qué eliges? ¿Piedra, papel o tijeras ?: ") .lower()
    jugador2 = input("¿Qué eliges? ¿Piedra, papel o tijeras ?: ") .lower ()


    condicion1 = jugador1 == "Piedra" and jugador2 == "tijeras" .lower()
    condicion2 = jugador1 == "papel" and jugador2 == "piedra" .lower()
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel" .lower()


    if jugador1 == jugador2:
        print ("Empate")
    elif condicion1 or condicion2 or condicion3:
        print ("Ha gando :", nombre1)
        puesto1 += 1
    else:
        print ("Ha gando :", nombre2)
        puesto2 += 1

    ronda += 1 



