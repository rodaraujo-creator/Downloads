usuario = (input("Ingrese el tipo de usuario (Estudiante, Adulto, Adulto Mayor): "))
horario = (input("Horario del viaje (Normal, Punta): "))

if usuario=="estudiante" :
    if horario == "normal" :
        print("La tarifa a pagar será de: $490")
    elif horario == "punta" :
        print("La tarifa a pagar será de $590")

if usuario == "adulto" :
    if horario == "normal" :
        print("La tarifa a pagar será de $790")
    elif horario == "punta" :
        print("La tarifa a pagar será de $890")

if usuario == 'adulto mayor' :
    if horario == 'normal' :
        print("La tarifa a pagar será de $390")
    elif horario == 'punta' :
        print("La tarifa a pagar será de $490")
print("Gracias por viajar con nosotros")
























