from random import randint

minimo = int(input("Limite Minimo:"))
maximo = int(input("Limite Máximo:"))

alea = randint(minimo,maximo)
print(f"Aleatorio:{alea}")

if alea % 2 == 0:
    alea = alea + 1
    print(f"por ser un número par se generará 10 impares partiendo de {alea}")
else:
    print(f"por ser impar se genera desde {alea}")
    
print(f"los impares partiendo de {alea} son:")
print(f" {alea} {alea+2} {alea+4} {alea+6} {alea+8} {alea+10} {alea+12} {alea+14} {alea+16}")