import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona con el nombre de: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        listaPersonas = open("ficheroExterno.txt", "ab+")
        listaPersonas.seek(0)

        try:
            self.personas = pickle.load(listaPersonas)
            print(
                "Se cargaron {} personas del ficehro externo".format(
                    len(self.personas))
            )
        except:
            print("El fichero esta vacio")
        finally:
            listaPersonas.close()
            del listaPersonas

    def AgregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def MostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaPersonas = open("ficheroExterno.txt", "wb")
        pickle.dump(self.personas, listaPersonas)
        listaPersonas.close()
        del listaPersonas

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)


miLista = ListaPersonas()

p = Persona("Carlos", "Masculino", 40)

miLista.AgregarPersonas(p)

miLista.mostrarInfoFicheroExterno()

# p=Persona("Amada","femenino",13)

# miLista.AgregarPersonas(p)

# p=Persona("Diana","femeninno",46)

# miLista.AgregarPersonas(p)

# miLista.MostrarPersonas()
