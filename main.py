# Funciones: sin parámetros / sin retorno
#           sin parámetros / con retorno
#           con parámetros / sin retorno
#           con parámetros / con retorno
#Evaluación: Listas, colecciones y funciones
#Proceso de ingresar, eliminar, listar, buscar y modificar.
# Contexto: Ingreso de productos en una tienda, cada producto
# posee: un codigo, nombre de producto, precio
#validacion: - codigo: numero positivo mayor a cero
#           - nombre: texto sin espacios y minimo tres caracteres.
#           - Precio: numero positivo entre 100 y 50000
lista_productos=[]
def validaCodigo(cod):
    try:
        c = int(cod)
        if c>0:
            return True
        return False
    except:
        return False
def validarNombre(nom):
    if len(nom.strip())>=3:
        return True
    return False
def validaPrecio(precio):
    try:
        p=int(precio)
        if p>=100 and p<=50000:
            return True
        return False
    except:
        return False  
def ingresarProducto(lista):
    codigo=input("Ingrese codigo del producto:")
    resp = validaCodigo(hh="hola", cod=codigo)
    if resp == False:
        print("Ingrese codigo numerico entero mayor a cero")
        return False
    nombre=input("ingrese nombre del producto:")
    resp = validarNombre(nombre)
    if resp==False:
        print("nombre sin espacios y minimo 3 letras")
        precio=input("ingrese precio del producto:")
        resp=validarNombre(nombre)
        if resp==False:
            print("nombre sin espacios y minimo 3 letras")
        return False
def menu():
    print("== menu almacen ==")
    print("1. Ingresar")
    print("2. Listar")
    print("3. Salir")

def seleccione():
    try:
        op=int(input("Seleccione:"))
        if op>=1 and op<=3:
            return op
        print("opciones entre 1 y 3")
        return op
    except:
        print("opcion incorrecta, ingrese solo numeros")
        return 0
    
    
def rutas(op):
    match op:
        case 1:
            print("== Ingresar ==")
        case 2:
            print("== Listar ==")
        case 3:
            print("== Salir ==")
ciclo = True
while ciclo:
    menu()
    opcion = seleccione()
    rutas(opcion)
    if opcion==3:
        ciclo=False

