class Factorial:
    def __init__(self):
        pass

    def calcular_factorial(self, num):
        """Calcula el factorial de un número."""
        if num < 0:
            print("Factorial de un número negativo no existe")
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        #Calcula los factoriales entre min_num y max_num, inclusive.
        for num in range(min_num, max_num + 1):
            print("Factorial de", num, "! es", self.calcular_factorial(num))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Debe ingresar dos numeros")
        sys.exit(1)

    min_num = int(sys.argv[1])
    max_num = int(sys.argv[2])

    if min_num < 1:
        print("El número mínimo debe ser mayor o igual a 1.")
        sys.exit(1)
    elif max_num > 60:
        print("El número máximo no puede ser mayor que 60.")
        sys.exit(1)
    elif min_num > max_num:
        print("El número mínimo no puede ser mayor que el número máximo.")
        sys.exit(1)

    factorial_calculator = Factorial()
    factorial_calculator.run(min_num, max_num)
