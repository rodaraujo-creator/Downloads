from random import randint

minimo=int(input("Indique Limite Mínimo:"))
maximo=int(input("Indique Limite Máximo:"))
aleatorio = randint(minimo,maximo)

if aleatorio % 2 != 0:
    #como es impar
    aleatorio = aleatorio - 1
    
print(f"{aleatorio} x 1 = {aleatorio*1}")
print(f"{aleatorio} x 2 = {aleatorio*2}")
print(f"{aleatorio} x 3 = {aleatorio*3}")
print(f"{aleatorio} x 4 = {aleatorio*4}")
print(f"{aleatorio} x 5 = {aleatorio*5}")
print(f"{aleatorio} x 6 = {aleatorio*6}")
print(f"{aleatorio} x 7 = {aleatorio*7}")
print(f"{aleatorio} x 8 = {aleatorio*8}")
print(f"{aleatorio} x 9 = {aleatorio*9}")
print(f"{aleatorio} x 10 = {aleatorio*10}")
print(f"{aleatorio} x 11 = {aleatorio*11}")
print(f"{aleatorio} x 12 = {aleatorio*12}")
