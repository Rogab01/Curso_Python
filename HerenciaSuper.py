class Persona():
    def __init__(self, nombre, edad, resideEn):
        self.nombre = nombre
        self.edad = edad
        self.resideEn = resideEn

    def descripcion(self):
        print("nombre: ", self.nombre, "edad: ",
              self.edad, "Reside: ", self.resideEn)
