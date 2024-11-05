import random

class Persona:
    def __init__(self, nombre, edad, sexo='H'):
        self.nombre = nombre
        self.edad = edad
        self.sexo = self.comprobar_sexo(sexo)
        self.dni = self.generaDNI()

    def es_mayor_edad(self):
        return self.edad >= 18

    def comprobar_sexo(self, sexo):
        if sexo.upper() in ['H', 'M']:
            return sexo.upper()
        else:
            print("Sexo introducido no válido. Se establece como 'H' por defecto.")
            return 'H'

    def generaDNI(self):
        dni_numero = random.randint(10000000, 99999999)
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        letra_dni = letras[dni_numero % 23]
        return str(dni_numero) + letra_dni

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nDNI: {self.dni}"


persona1 = Persona("Muhammed", 99, "H")
print(persona1)
print("¿Es mayor de edad?", persona1.es_mayor_edad())

persona2 = Persona("Agata", 2, "M")
print(persona2)
print("¿Es mayor de edad?", persona2.es_mayor_edad())