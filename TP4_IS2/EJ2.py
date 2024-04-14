from __future__ import annotations
from abc import ABC, abstractmethod

class Lamina:
    def __init__(self, tren: TrenLaminador) -> None:
        self.tren = tren

    def producir(self) -> str:
        return (f"Lamina: Producción con:\n"
                f"{self.tren.producir_lamina()}")

class TrenLaminador(ABC):
    @abstractmethod
    def producir_lamina(self) -> str:
        pass

class TrenLaminador5Mts(TrenLaminador):
    def producir_lamina(self) -> str:
        return "TrenLaminador5Mts: Generando lámina de acero de 5 mts."

class TrenLaminador10Mts(TrenLaminador):
    def producir_lamina(self) -> str:
        return "TrenLaminador10Mts: Generando lámina de acero de 10 mts."

def client_code(lamina: Lamina) -> None:
    print(lamina.producir(), end="")

if __name__ == "__main__":
    tren = TrenLaminador5Mts()
    lamina = Lamina(tren)
    client_code(lamina)

    print("\n")

    tren = TrenLaminador10Mts()
    lamina = Lamina(tren)
    client_code(lamina)

    print("\n")