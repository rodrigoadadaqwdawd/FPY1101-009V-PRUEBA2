from random import randint

flag_numero = True
while flag_numero:
    try:
        numero1 = int(input("Porfavor ingrese el primer número: "))
        numero2 = int(input("Porfavor ahora ingrese el segundo número: "))
        if numero1 < numero2:
            numero = randint(numero1, numero2)
            flag_numero = False
        else:
            print("El primer numero debe ser menor al segundo numero, intente de nuevo")
    except ValueError:
        print("Debe ingresar un numero entero, intente de nuevo")


if numero % 2 != 0:
    numero += 1
    if numero > numero2:
        numero -= 2

while True:
    intento1 = int(input("Debe adivinar el numnero: "))
    if intento1 < numero:
        print("El numero es mayor")
    elif intento1 == numero:
        print("felicidades adivinaste el numero al primer intento")
        break
    else:
        print("El numero es menor")
        

    intento2 = int(input("Intento fallido, segundo intento: "))
    if intento2 < numero:
        print("El numero es mayor")
    elif intento2 == numero:
        print("felicidades adivinaste el numero al segundo intento")
        break  
    else:    
     print("El numero es menor")

    distancia1 = abs(numero - intento1)
    distancia2 = abs(numero - intento2)
    if distancia1 < distancia2:
        print("El primer intento estuvo mas cerca")
    else:
        print("El segundo intento estuvo mas cerca")

    intento3 = int(input("Intento fallido, ultimo intento: "))
    if intento3 < numero or intento3 > numero:
        print("perdiste, el numero era: ", numero)
        break
    else:
        print("felicidades adivinaste en el ultimo intento")
        break
