# Mensaje de bienvenida al supermercado
print('''    
    Supermercado La Fama
------------------------------
        Bienvenidos
        ''')

# Se desea crear un sistema que permita determinar el descuento que tendrá un cliente en su compra dependiendo de su edad, estado civil y si es socio del supermercado.

monto=int(input("Ingrese monto: "))
edad=int(input("Ingrese edad: "))
estadocivil=input("Ingrese estado civil: ")
sociocheck=input("¿Eres Socio de FamaClub? (S/N): ")

# Preguntar si el tipo es mayor de 70 y si es soltero/viudo
if edad > 70 :
    if estadocivil == "soltero" or estadocivil == "viudo" :
        descuento = monto * 0.15
    elif estadocivil == "casado" or estadocivil == "divorciado":
        descuento = monto * 0.10
    print(f"Tu monto a pagar: ${monto-descuento}")
    print(f"Tu descuento fue: ${descuento}")
if edad >= 25 and edad <= 69:
    if estadocivil == "soltero" or estadocivil == "viudo":
        descuento = monto * 0.05
    elif estadocivil == "casado" or estadocivil == "divorciado":
        descuento = monto * 0.03
    print(f"Tu monto a pagar: ${monto-descuento}")
    print(f"Tu descuento fue: ${descuento}")
if sociocheck == "S":
    descuento += monto * 0.08
    print(f"Tu monto a pagar: ${monto-descuento}")
    print(f"Tu descuento fue: ${descuento}")