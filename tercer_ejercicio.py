continuar = True
pila = list()
while continuar == True:
    numero = int(input("ingrese un numero: "))
    pila.append(numero)
    agregar = int(input("desea agregar otro numero?" "1 para si u otro numero para no "))
    print(numero)
    if agregar!=1:
        continuar = False
print(pila)
suma = 0
'''
for i in pila:
    suma = suma + i
'''
cantidades_restantes = len(pila)
print(f"cantidad d elementos que hay en la lista{cantidades_restantes}")
i = cantidades_restantes - 1
print(f"el indice del ultimo elemento ingresado y q se va a eliminaar es: {i}")
while i>=0:
    element = pila.pop()
    print(f"el elemento que se saco de la pila fue {element}")
    suma = suma + element
    i = i-1

print(f"la suma de los nuemeros agregados es = {suma}")
