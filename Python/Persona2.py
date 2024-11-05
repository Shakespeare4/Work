class  Persona():
 # Constructor
    def init(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print("Hola me llamo", self.nombre, "mi edad es", self.edad)


if __name__ == 'main':
    a = [["Perpito", 10], ["Juanito", 20], ["Jorge", 50]]
    for person in a:
        Persona(person[0], person[1]).presentar()

    '''
    p1 = Persona("Juan", 10)
    p1.presentar()

    p2 = Persona("Carlos", 20)
    p2.presentar()
    '''