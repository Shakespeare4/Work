class Persona:
    #Constructor
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print("Hola me llamo", self.nombre, "mi edad es de", self.edad)

if __name__ == '__main__':
    p1 = Persona("Juan", 10)
    p1.presentar()

    p2 = Persona("Carlos", 20)
    p2.presentar()