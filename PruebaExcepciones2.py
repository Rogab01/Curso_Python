def divide():
    try:
        op1 = float(input("Introduce el primer numero: "))

        op2 = float(input("Introduce el segundo numero: "))

        print("la division es: " + str(op1/op2))

    except ValueError:

        print("El valor introdcido es erroneo!!!")

    except ZeroDivisionError:

        print("No se puede dividir por cero!!!")

    finally:
        print("calculo finalizado")


divide()
