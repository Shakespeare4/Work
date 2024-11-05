class Cuenta:
    def _init__(self, NumCuenta, DNI, saldoactual, interesanual):
        self.NumCuenta = int(NumCuenta)
        self.DNI = int(DNI)
        self.saldoactual = saldoactual
        self.interesanual = interesanual 
    
    def actualizar_saldo(self):
        interes_diario = (self.interesanual / 100) / 365
        self.saldoactual += self.saldoactual * interes_diario
     
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldoactual += cantidad
            print("Cantidad ingresada ", cantidad)
        else:
            print("No se puede ingresar una cantidad inexistente")

    def retirar(self, cantidad):
        if cantidad > 0 and self.saldoactual >= cantidad:
            self.saldoactual -= cantidad
            print("Cantidad retirada ", cantidad)
        else:
            print("No se puede retirar esa cantidad, no te basta el dinero. Pobre. Tambien es posible que la cantidad no sea valida.")
    def mostrar_datos(self):
        print("Número de cuenta:", self.NumCuenta)
        print("DNI del cliente:", self.DNI)
        print("Saldo actual:", self.saldoactual)
        print("Interés anual:", self.interesanual)

cuenta_ejemplo = Cuenta()

cuenta_ejemplo.NumCuenta = int(input("Introduce el número de cuenta: "), base = 0)
cuenta_ejemplo.DNI = int(input("Introduce el DNI del cliente: "), base = 0)
cuenta_ejemplo.saldoactual = float(input("Introduce el saldo actual: "),)
cuenta_ejemplo.interesanual = float(input("Introduce el interés anual (en porcentaje): "))

cuenta_ejemplo.mostrar_datos()
cuenta_ejemplo.mostrar_datos()
cuenta_ejemplo.actualizar_saldo()
print("Saldo actualizado con interés:", cuenta_ejemplo.saldoactual)
cantidad_ingreso = float(input("Introduce la cantidad a ingresar: "))
cuenta_ejemplo.ingresar(cantidad_ingreso)
cantidad_retiro = float(input("Introduce la cantidad a retirar: "))
cuenta_ejemplo.retirar(cantidad_retiro)
cuenta_ejemplo.mostrar_datos()