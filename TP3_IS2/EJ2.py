class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ImpuestosCalculator(metaclass=SingletonMeta):
    def calculate_impuestos(self, costoBase):
        VAT = 0.21
        IIBB = 0.05
        contibucionesMunicipales= 0.012

        totalImpuestos= costoBase * (VAT + IIBB + contibucionesMunicipales)
        return totalImpuestos


if __name__ == "__main__":
    calculator1 = ImpuestosCalculator()
    calculator2 = ImpuestosCalculator()
    num=int(input('Ingrese el valor de lo comprado:'))

    if id(calculator1) == id(calculator2):
        print("Singleton Funciona, ambas variables contienen la misma instancia.")
        print("El impuesto total para el monto es: ", calculator1.calculate_impuestos(num))
    else:
        print("Singleton fallo, variables contain different instances.")