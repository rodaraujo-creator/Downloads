print("Bienvenido al Cine Regional")
user=input("Ingrese nombre de usuario: ")
passwd=int(input("Ingrese contraseña: "))

publico=input("Ingrese el tipo de público (Normal, Estudiante, Adulto Mayor): ")
sala=input("Seleccione tipo de sala (Normal, 3D, 4DX): ")
entradas=int(input("Ingrese cantidad de entradas: "))
print(f"Cantidad de entradas: {entradas}")
precio=0
if publico == "normal" :
    if sala == "normal" :
        print("Subtotal: $5600")
        precio=5600
    elif sala == "3D" :
        print("Subtotal: $7800")
        precio=7800
    elif sala == "4DX" :
        print("Subtotal: $12000")
        precio=12000
if publico == "estudiante" :
    if sala == "normal" :
        print("Subtotal: $3400")
        precio=3400
    elif sala == "3D" :
        print("Subtotal: $4800")
        precio=4800
    elif sala == "4DX" :
        print ("Subtotal: $7000")
        precio=7000
if publico == "adulto mayor" :
    if sala == "normal" :
        print("Subtotal: $2500")
        precio = 2500
    elif sala == "3D" :
        print("Subtotal: $3500")
        precio=3500
    elif sala == "4DX" :
        print ("Subtotal: $4800")
        precio=4800
        
print("IVA: $2660")
subtotal = precio * entradas
iva = subtotal * 0.19
print("-" * 45)
total = subtotal + iva
print(f"Total: {total}")