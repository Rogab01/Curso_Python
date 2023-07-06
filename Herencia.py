class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def Arrancar(self):
        self.enmarcha = True

    def Acelerar(self):
        self.acelera = True

    def Frenar(self):
        self.frena = True

    def Estado(self):
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
    def Carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


# fin de clase
class Moto(Vehiculo):
    hcaballito = ""

    def Caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def Estado(self):
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
class Velectricos:
    def __init__(self):
        self.autonomia = 100

    def CargarEnergia(self):
        self.cargando = True


miMoto = Moto("Honda", "CBR")
miMoto.Caballito()
miMoto.Estado()
print("********* furgoneta *********")
miFurgoneta = Furgoneta("Renault", "Kango")
miFurgoneta.Arrancar()
miFurgoneta.Estado()
print(miFurgoneta.Carga(True))


class BiciElectrica(Velectricos, Vehiculo):
    pass


miBici = BiciElectrica()
miBici.Estado()
