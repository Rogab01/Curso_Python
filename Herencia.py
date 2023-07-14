class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            "Marca: ",
            self.marca,
            "\nModelo: ",
            self.modelo,
            "\nEn Marcha: ",
            self.enmarcha,
            "\nAcelerando: ",
            self.acelera,
            "\nFrenando: ",
            self.frena,
        )


# fin de clase
class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


# fin de clase
class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print(
            "Marca: ",
            self.marca,
            "\nModelo: ",
            self.modelo,
            "\nEn Marcha: ",
            self.enmarcha,
            "\nAcelerando: ",
            self.acelera,
            "\nFrenando: ",
            self.frena,
            "\nEstado: ",
            self.hcaballito,
        )


# fin de clase
class VElectricos:
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

print("********* furgoneta *********")
miFurgoneta = Furgoneta("Renault", "Kango")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


class BiciElectrica(VElectricos, Vehiculo):
    pass


miBici = BiciElectrica()
miBici.estado()
