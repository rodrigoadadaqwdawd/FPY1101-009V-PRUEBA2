flag_edad_usuario = True
while flag_edad_usuario == True:
    try:
        edad = int(input("Porfavor ingresar su edad: "))
        if edad <= 0:
            print("ERROR, la edad tiene que ser sobre 0")
        else:
            flag_edad_usuario = False
    except:  
            print("Debes ingresar un numero entero para la edad")

flag_tramo_usuario = True
while flag_tramo_usuario == True:
     tramo = input("Porfavor ingresar su tramo (A, B, C o D): ").upper()
     if tramo == "A" or tramo == "B" or tramo == "C" or tramo == "D":
         flag_tramo_usuario = False
     else:
         print("ERROR, el tramo tiene que ser A, B, C o D")

valor_mensual_medicamento = 60000
valor_despacho_domicilio = 8000

valor_final_medicamento = 0
valor_final_despacho = 0
descuento = 0
descuento_despacho = 0
total = 0

if edad <= 30 and tramo in ("A", "B"):
    descuento = 0.18
elif edad <= 30 and tramo in ("C", "D"):
    descuento = 0.12
elif edad >= 31 and edad <= 60 and tramo in ("A", "B"):
    descuento = 0.12
elif edad >= 31 and edad <= 60 and tramo in ("C", "D"):
    descuento = 0.08
else:
    descuento = 0

if tramo == "A" or tramo == "B":
    if edad >= 55 and edad <= 60:
        descuento_despacho = 0.15
    else:
        descuento_despacho = 0.1

valor_final_medicamento = int(valor_mensual_medicamento - (valor_mensual_medicamento*descuento))
valor_final_despacho    = int(valor_despacho_domicilio - (valor_despacho_domicilio*descuento_despacho))
total = valor_final_medicamento + valor_final_despacho

#Imprimiendo resultados
print (f"El valor final de su medicamento es: ${valor_final_medicamento}")
print (f"El valor final de su despacho es: ${valor_final_despacho}")
print (f"El valor total de su medicamento y su despacho es {total}")
