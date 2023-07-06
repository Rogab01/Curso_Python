print("Programa de Evaluación de Notas de Alumnos")

notaAlumno = input("Introduce la Nota del Alumno: ")


def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspendido"
    return valoracion


print(evaluacion(int(notaAlumno)))
