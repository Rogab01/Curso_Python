class Coche():
    def desplazamiento(self):
        print("Me desplazo utlizando cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utlizando dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utlizando seis ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

miVehiculo4 = Moto()
desplazamientoVehiculo(miVehiculo4)
