class Persona():
    def __init__(self, nombre, edad, resideEn):
        self.nombre = nombre
        self.edad = edad
        self.resideEn = resideEn

    def descripcion(self):
        print("nombre: ", self.nombre, "edad: ",
              self.edad, "Reside: ", self.resideEn)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, resideEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, resideEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("salario: ", self.salario, "Antiguedad: ", self.antiguedad)


antonio = Persona("Antonio", 46, "España")
antonio.descripcion()

antonia = Empleado(1500, 15, "antonia", 46, "colombia")

antonia.descripcion()

# la instruccion isinstance nos dice si un objeto pertence a una clase

print(isinstance(antonio, Empleado))
