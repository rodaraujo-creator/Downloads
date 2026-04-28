acum=0
descuento=0
subtotal=0
cantidad=0
ciclo = True
while ciclo:
    print('''
    Producto            Unidades Medida           Precio
    -----------------------------------------------------
    1) Lipigas          15 kilos                  $15.500
    2) Gasco            11 kilos                  $10.000
    3) Gasco            15 kilos                  $13.000
    4) Abastible        45 kilos                  $45.000
    ''')
    
    op = int(input("Seleccione: "))
    if op >=1 and op <=4 :
        cantidad = int(input("Ingrese cantidad: "))
    match op:
        case 1:
            subtotal = 15500 * cantidad
        case 2:
            subtotal = 10000 * cantidad
        case 3:
            subtotal = 13000 * cantidad
        case 4:
            subtotal * 45000 * cantidad
        case 5:
            ciclo = False
        case 6:
            acum = 0
        case _:
            print("Opción incorrecta")
    print (f"Tu subtotal es: {subtotal}")
    if op!=2 and cantidad>=3:
        match op:
                case 1:
                    descuento = subtotal * 0.1
                case 3:
                    descuento = subtotal * 0.05
                case 4:
                    descuento = subtotal * 0.03
    print(f"Total a pagar: {subtotal-descuento}")
    acum = acum + (subtotal-descuento)
    subtotal=0
    descuento=0
    print(f"Total a pagar: {acum}")