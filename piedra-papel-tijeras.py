nombre1 = input ("¿Cómo se llamara el jugador 1?: ")
print (nombre1.lower())
nombre2 = input ("¿Cómo se llamara el jugador 2?: ")
print (nombre2.lower())


jugador1 = input("Hola jugador1, ¿que eliges? ¿Piedra papel o tijeras?: " ,) .lower()
jugador2 = input("Hola jugador2, ¿que eliges? ¿Piedra papel o tijeras?: ", ) .lower()


#CONDICIONES---------
condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"


if jugador1 == jugador2:
    print ("Empate")
elif condicion1 or condicion2 or condicion3:
    print ("Ha ganado : ", nombre1)    
else:
    print ("Ha ganado : ", nombre2)

