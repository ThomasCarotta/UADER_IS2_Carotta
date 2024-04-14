class Componente():
    def operacion(self) -> float:
        pass

class Numero(Componente):
    def __init__(self, valor: float) -> None:
        self.valor = valor

    def operacion(self) -> float:
        return self.valor

class Decorador(Componente):
    _componente: Componente = None

    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    @property
    def componente(self) -> Componente:
        return self._componente

    def operacion(self) -> float:
        return self._componente.operacion()

class SumarDos(Decorador):
    def operacion(self) -> float:
        return self.componente.operacion() + 2

class MultiplicarPorDos(Decorador):
    def operacion(self) -> float:
        return self.componente.operacion() * 2

class DividirPorTres(Decorador):
    def operacion(self) -> float:
        return self.componente.operacion() / 3

def codigo_cliente(componente: Componente) -> None:
    print(f"RESULTADO: {componente.operacion()}", end="")

if __name__ == "__main__":
    valor = float(input("Introduce un número: "))
    simple = Numero(valor)
    print("Cliente: Tengo un componente simple:")
    codigo_cliente(simple)
    print("\n")

    operacion = input("Elige una operación (a: sumar 2, b: multiplicar por 2, c: dividir por 3): ")
    if operacion == 'a':
        decorador = SumarDos(simple)
    elif operacion == 'b':
        decorador = MultiplicarPorDos(simple)
    elif operacion == 'c':
        decorador = DividirPorTres(simple)
    else:
        print("Operación no válida.")
        exit(1)

    print("Cliente: Ahora tengo un componente decorado:")
    codigo_cliente(decorador)

    print("\n")