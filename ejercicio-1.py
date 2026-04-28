# Ejemplo como lo pide la rúbrica
print("Dristribuidora de gas 'Los Lindos'")
descuento = 0
subtotal = 0
print('''
    Producto            Unidades Medida           Precio
    -----------------------------------------------------
    1) Lipigas          15 kilos                  $15.500
    2) Gasco            11 kilos                  $10.000
    3) Gasco            15 kilos                  $13.000
    4) Abastible        45 kilos                  $45.000
    ''')


opcion = int(input("Seleccione:"))
if opcion <=0 or opcion >4 :
    print("Opción incorrecta")
else :
    cantidad = int(input("Cantidad de cilindros: "))
    if cantidad <=0 :
        print("Ingresó una cantidad incorrecta")
    else:
        if opcion == 1:
            subtotal = 15500 * cantidad
        elif opcion == 2:
            subtotal = 10000 * cantidad
        elif opcion == 3:
            subtotal = 13000 * cantidad
        else:
            subtotal = 45000 * cantidad
        print(f"Su subtotal es de {subtotal}")
        
        if cantidad >=3 and opcion !=2 :
            if opcion == 1:
                descuento = subtotal * 0.1
            if opcion == 3:
                descuento = subtotal * 0.05
            else:
                descuento = subtotal * 0.03
            print(f"tiene descuento el cual es de {descuento}")
        print(f"Total a pagar: {subtotal-descuento}")