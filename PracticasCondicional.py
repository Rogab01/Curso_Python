edad = 7

if 0 < edad < 100:  # concatenacion de operador
    print("Edad es correcta")
else:
    print("Edad Incorrecta")

print("----------------------------------------------------------------------------")
print("Evaluar Salario del presidente de la empresa, del administrador y del secretario")


salario_presidente = int(input("Introduce el salario del presidente: "))
print("salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce el salario del Director: "))
print("salario director: " + str(salario_director))

salario_administrador = int(input("Introduce el salario del Administrador: "))
print("salario Administrador: " + str(salario_administrador))

salario_secretario = int(input("Introduce el salario del Secretario: "))
print("salario del secretario: " + str(salario_secretario))

if salario_secretario < salario_administrador < salario_director < salario_presidente:
    print("Todo funciona bien, todo mono")
else:
    print("Algo falla en la empresa, huele mal")


print("----------------------------------------------------------------------------")
print("Programa de becas a estudiante 2020")

distancia_escuala = int(input("Introcude la distancia a la escuela en Km: "))
print(distancia_escuala)

numero_hermanos = int(input("Cuantos hermanos son: "))
print(numero_hermanos)

sali_familiar = int(input("Introduce el salario Bruto: "))
print(sali_familiar)

# operador logico AND y OR
if distancia_escuala > 40 and numero_hermanos > 2 or sali_familiar <= 20000:
    print("Tienes derecho a Beca")
else:
    print("pailas no tienes derecho a Beca")


print("----------------------------------------------------------------------------")
print("Asignaturas Optativas año 2020")
print("1: Informatica Grafica - 2: Pruebas de Software - 3: Usabilidad y Accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

# operador logico IN
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no esta permitida")
