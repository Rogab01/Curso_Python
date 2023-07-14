class Coche():

    def __init__(self):  # se usa los __ para indicar que es el inicializador de la clase
        # se usan los __ para encapsular las variables, evitaacceder a la variable desde fuera de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()

        if (self.__enMarcha and chequeo):
            return "el carro esta en marcha"

        elif (self.__enMarcha and chequeo == False):
            return "algo ha ido mal en el chequo"
        else:
            return "El carro esta apagado"

    def estado(self):
        print("El carro tiene ", self.__ruedas, " ruedas, un ancho de ",
              self.__anchoChasis, " y un largo ", self.__largoChasis)

    # los __ en los metodos se usan para ancapsular - los hacen de uso interno de la clase
    def __chequeoInterno(self):
        print("Realizando chequeo interno")

        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if (self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
            return True
        else:
            return False


miCarro = Coche()
# print("el largo del carro es: ", miCarro.largoChasis)
# print("el ancho del carro es: ", miCarro.anchoChasis)
# print("El carro tiene: ", miCarro.ruedas)
print(miCarro.arrancar(True))
miCarro.estado()


print("************ Creando segundo Objeto ************")

miCarro2 = Coche()
# print("el largo del carro es: ", miCarro2.largoChasis)
# print("el ancho del carro es: ", miCarro2.anchoChasis)
# print("El carro tiene: ", miCarro2.ruedas)
print(miCarro2.arrancar(False))
# micarro2.__ruedas=2
miCarro2.estado()
