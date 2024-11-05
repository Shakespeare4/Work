import random 
num = random.randint(1,10)
input = input("Dime un numero ")

while not True:
    if int(input) <= num:
        print("Incorrecto, el correcto es mayor")
        print(int(input))
        
    elif int(input) >= num:
        print("Incorrecto, el correcto es menor")
        print(input)

    else:
        print("CORRECTO")
        True = False 