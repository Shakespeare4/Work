class Coche():
    def init(self, nombre, velocidad_actual, velocidad_maxima):
        self.nombre = nombre
        self.velocidad_actual = velocidad_actual
        self.velocidad_maxima = velocidad_maxima
        self.estado = 0
    def arranca(self):
        print("El coche", self.nombre, "arranca a ", self.velocidad_actual)
        if self.estado == 0:
            self.estado +1 
    def acelera(self):
        print()