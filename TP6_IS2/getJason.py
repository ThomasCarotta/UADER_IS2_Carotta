import json
import sys

VERSION = "versión 1.2"

class LectorJSONSingleton:
    """
    Implementacion de un patrón Singleton para lectura de archivo JSON.
    """
    def __new__(cls, ruta_archivo):
        if not hasattr(cls, '_instancia'):
            cls._instancia = super().__new__(cls)
            cls._instancia.ruta_archivo = ruta_archivo
            cls._instancia.info_bancos = cls._instancia._cargar_info_bancos()
        return cls._instancia

    def _cargar_info_bancos(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = archivo.read()
            objeto_json = json.loads(datos)
            return objeto_json.get("bancos", {})
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ruta_archivo} .")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: El archivo no es un JSON .")
            sys.exit(1)

    def obtener_info_bancos(self):
        """
        Obtencion de la información de los bancos.
        """
        return self.info_bancos


class Banco:
    def __init__(self, nombre, saldo_inicial, token):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.token = token

    def puede_procesar(self, monto):
        """
        Verificaciondel proceco del pago.
        """
        return self.saldo >= monto

    def procesar_pago(self, monto):
        """
        Procesamiento del pago.
        """
        if self.puede_procesar(monto):
            self.saldo -= monto
            return True
        return False

    def obtener_info_pago(self, monto):
        """
        Retorno de la información del pago.
        """
        return {
            'nombre_banco': self.nombre,
            'monto': monto,
            'token': self.token
        }

    def __str__(self):
        return f"Banco {self.nombre} - Saldo: {self.saldo} - Token: {self.token}"


class Pago:
    def __init__(self, numero_orden, nombre_banco, monto, token):
        self.numero_orden = numero_orden
        self.nombre_banco = nombre_banco
        self.monto = monto
        self.token = token

    def __str__(self):
        return (f"Orden {self.numero_orden}: Banco {self.nombre_banco}, "
                f"Monto {self.monto}, Token {self.token}")


class HistorialPagos:
    """
    historial de pagos.
    """
    def __init__(self):
        self.pagos = []

    def agregar_pago(self, pago):
        self.pagos.append(pago)

    def __iter__(self):
        return iter(self.pagos)


class ManejadorPagos:
    def __init__(self, banco, sucesor=None):
        self.banco = banco
        self.sucesor = sucesor

    def manejar(self, monto, numero_orden, historial_pagos):
        """
        interaccion con el banco actual
        """
        if self.banco.procesar_pago(monto):
            info_pago = self.banco.obtener_info_pago(monto)
            pago = Pago(numero_orden, info_pago['nombre_banco'], monto, info_pago['token'])
            historial_pagos.agregar_pago(pago)
            print(f"El monto del pago fue de ${monto} y fue procesado por el banco {self.banco.nombre}. Siendo su saldo ahora de: ${self.banco.saldo}")
            return True
        if self.sucesor is not None:
            return self.sucesor.manejar(monto, numero_orden, historial_pagos)
        print(f"Error: su pago de ${monto} no fue procesado ya que su saldo es insuficiente.")
        return False


class CadenaBancos:
    def __init__(self, bancos):
        self.cadena = None
        for banco in bancos:
            self.cadena = ManejadorPagos(banco, self.cadena)

    def procesar_pago(self, monto, numero_orden, historial_pagos):
        """
        Procesamiento del pago.
        """
        if self.cadena is not None:
            return self.cadena.manejar(monto, numero_orden, historial_pagos)
        print("Error: No se puede procesar el pago ya que no hay bancos disponibles.")
        return False


class Programa:
    def __init__(self, cadena_bancos, historial_pagos):
        """
        Constructor de la clase Programa.
        """
        self.cadena_bancos = cadena_bancos
        self.historial_pagos = historial_pagos
        self.numero_orden = 0

    def ejecutar(self, opcion, monto=None):
        """
        Método principal del programa.
        """
        try:
            if opcion == "auto":
                if monto is None:
                    print("Error: Se requiere un monto para la opción 'auto'")
                    sys.exit(1)
                self.numero_orden += 1
                self.cadena_bancos.procesar_pago(float(monto), self.numero_orden, self.historial_pagos)
            elif opcion == "lista":
                realizar_multiples_pagos(self)
            else:
                print("Error: Opción inválida.")
                imprimir_uso()
                sys.exit(1)
        except Exception as err:
            print(f"Error del programa: {err}")
            sys.exit(1)


def realizar_multiples_pagos(programa):
    """
    Función que ejecuta múltiples pagos y los almacena en el historial de pagos.
    """
    try:
        for _ in range(5):
            programa.numero_orden += 1
            monto = 500.0
            programa.cadena_bancos.procesar_pago(monto, programa.numero_orden, programa.historial_pagos)
    except ValueError:
        print("Error: El monto es inválido.")


def imprimir_uso():
    """
    Función que implementa una ayuda para el manejo del programa.
    """
    print("Modo de uso: py programa.py <archivo_json> <opcion> [<monto>]")
    print("Opciones:")
    print("auto: Automáticamente elige un banco para procesar el pago basado en el monto especificado")
    print("lista: Ejecuta múltiples pagos y los almacena en el historial")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        print(f"Programa: {VERSION}")
        sys.exit(0)

    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        imprimir_uso()
        sys.exit(0)

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error del programa: argumentos inválido.")
        imprimir_uso()
        sys.exit(1)

    ruta_archivo_json = sys.argv[1]
    opcion = sys.argv[2]
    monto_pago = sys.argv[3] if len(sys.argv) == 4 else None

    try:
        bancoA = Banco("Banco Nacion", 1000.0, "token1")
        bancoB = Banco("Santander", 2000.0, "token2")

        cadena_bancos = CadenaBancos([bancoA, bancoB])

        historial_pagos = HistorialPagos()

        programa = Programa(cadena_bancos, historial_pagos)
        programa.ejecutar(opcion, monto_pago)
    except Exception as err:
        print(f"Error del programa: {err}")
        sys.exit(1)
