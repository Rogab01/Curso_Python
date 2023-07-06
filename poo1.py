class Coche():

	def __init__(self):
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def Arrancar(self,arracamos):
		self.__enmarcha=arracamos

		if(self.__enmarcha):
			chequeo=self.__ChequeoInterno()

		if (self.__enmarcha and chequeo):
			return "el carro esta en marcha"

		elif (self.__enmarcha and chequeo==False):
			return "algo ha ido mal en el chequo"
		else:
			return "El carro esta apagado"

	def Estado(self):
		print("El carro tiene ",self.__ruedas," ruedas, un ancho de ",self.__anchoChasis," y un largo ",self.__largoChasis)

	def __ChequeoInterno(self):
		print("Realizando chequeo interno")

		self.gasolina="Ok"
		self.aceite="Ok"
		self.puertas="Cerradas"

		if(self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
			return True
		else:
			return False
		

micarro=Coche()
#print("el largo del carro es: ", micarro.largoChasis) 
#print("el ancho del carro es: ", micarro.anchoChasis) 
#print("El carro tiene: ", micarro.ruedas)
print(micarro.Arrancar(True))
micarro.Estado()


print("********** Creando segundo Objeto **********")

micarro2=Coche()
#print("el largo del carro es: ", micarro2.largoChasis) 
#print("el ancho del carro es: ", micarro2.anchoChasis) 
#print("El carro tiene: ", micarro2.ruedas)
print(micarro2.Arrancar(False))
#micarro2.__ruedas=2

