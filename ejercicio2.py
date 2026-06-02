def suma():
    num1=int(input("Numero 1:"))
    num2=int(input("Numero 2:"))
    print(f"La suma es {num1+num2}")
    
def resta():
    num1=int(input("Numero 1:"))
    num2=int(input("Numero 2:"))
    print(f"La resta es {num1-num2}")
    
ciclo=True
while ciclo:
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Salir")
    op = int(input("Seleccione:"))
    
    match op:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            ciclo=False