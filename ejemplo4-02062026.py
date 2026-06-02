# funcion que recibe 2 parámetros
# son NUM1, NUM2 y luego retorna
# el resultado
def sumar(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Ingrese numero 1:"))
n2=int(input("Ingrese numero 2:"))
s = sumar(n1, n2)
print(f"La suma es {s}")