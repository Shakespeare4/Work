#Recorrido==for
#Busqueda==while
a = ["marco", "macia", "juan", "toni", "jonathan"]

def recorrido():
    for i in a:
        print(i)
def busqueda():
    index = 0
    while index <= len(a):
     if a[index] == "juan":
        print(a[index], "esta en la posicion", index)
        break  
     index = index + 1  
def funcionforconwhile():
    index = 0
    while index <= len(a):
            print(a[index])
            break  
    index = 0 + 1
palabra = ["m", "a", "c", "i", "a"]
letras = []
contadorlnum = []
def detectar_letras():
    for letra in palabra:
        if letra not in letras:
            letras.append(letra)
    print(letras)

def contador():
    for letra in letras:
            contadorlnum.append(letra)
    print(contadorlnum)



if __name__ == "__main__":
    contador()