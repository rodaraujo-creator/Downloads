monto_pagar=0
flag_matricula =False
flag_cp = False
print("Bienvenido al Colegio 'Republica de Chillan'")
print('''
    Indique concepto a pagar:
    1) matrícula Básica
    2) matrícula Media
    '''
    )
opcion = int(input("Seleccione:"))
if opcion == 1:
    monto_pagar = 45000
elif opcion == 2:
    monto_pagar = 67000
else:
    print("Opción incorrecta")
opcion2=input("Pagará Centro de Padres (S/N):").upper()
if opcion2 == "S":
    print("Se incluirá el cobro de centro de padres de $10.000 pesos")
    monto_pagar += 10000
opcion3=input("¿Pagará Mensualidad? (S/N):").upper()
if opcion3 == "S":
    cuantas = int(input("Indique mensualidades a pagar (1 a 12):"))
    mensualidad =0
    descuento = 0
    if cuantas >=3 and cuantas<=5:
        mensualidad = cuantas*30000
        descuento = mensualidad*0.06
        print(f"Se aplicará un descuento de 6% {descuento}")
    elif cuantas>=6 and cuantas<=11:
        mensualidad = cuantas*30000
        descuento = mensualidad*0.1
        print(f"Se aplicará un descuento de 10% {descuento}")
    elif cuantas==12 and (opcion==1 or opcion==2) and opcion2=="S":
        mensualidad = cuantas*30000
        descuento = mensualidad * 0.2
        print(f"Se aplicará un descuento de 20% {descuento}")
    else:
        print("No hay descuento")
        mensualidad=cuantas*30000
    print(f"Total a pagar en mensualidades {mensualidad-descuento}")
monto_pagar += mensualidad-descuento
print(f"Total:{monto_pagar}")
