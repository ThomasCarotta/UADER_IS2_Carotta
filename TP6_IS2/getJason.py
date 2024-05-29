# # uncompyle6 version 3.9.1
# # Python bytecode version base 3.6 (3379)
# # Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)]
# # Embedded file name: getJason.py
# # Compiled at: 2022-06-14 16:15:55
# # Size of source mod 2**32: 214 bytes

# import json, sys
# jsonfile = sys.argv[1]
# jsonkey = sys.argv[2]
# with open(jsonfile, "r") as myfile:
#     data = myfile.read()
# obj = json.loads(data)
# print(str(obj[jsonkey]))

#------------------Vercion ejercicio 3------------------
# #copyright UADER FCyT-IS2©2024 todos los derechos reservados

# import json
# import sys

# class SingletonMeta(type):
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]

# class TokenExtractor(metaclass=SingletonMeta):
#     version = "[1.1]"

#     def __init__(self, jsonfile="", jsonkey="token1"):
#         """
#         Inicializa el extractor de token con el archivo JSON y la clave especificados.
#         """
#         self.jsonfile = jsonfile
#         self.jsonkey = jsonkey

#     def print_help(self):
#         """
#         Imprime el mensaje de ayuda del programa.
#         """
#         help_message = """
# Extractor de token para acceso API Servicios Banco XXX (versión 1.1)

# Este programa permite extraer la clave de acceso API para utilizar los servicios del 
# Banco XXX.

# El programa operará como un microservicio invocado mediante:s

#     {path ejecutable}/getJason.py {path archivo JSON}/{nombre archivo JSON}.json [clave]

# ej.
#     ./getJason.py ./sitedata.json token1

# El token podrá recuperarse mediante el standard output de ejecución en el formato

#     {1.1}XXXX-XXXX-XXXX-XXXX

# Para obtener un mensaje de ayuda detallado ejecutar

#     ./getJason.py -h

# Excepciones

# Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
# terminar.
# """
#         print(help_message)

#     def print_version(self):
#         """
#         Imprime la versión del programa.
#         """
#         print(f"Versión {self.version}")

#     def extract_token(self):
#         """
#         Extrae el token del archivo JSON utilizando la clave especificada.
#         """
#         try:
#             with open(self.jsonfile, "r") as myfile:
#                 data = myfile.read()
#             obj = json.loads(data)
#             token = str(obj[self.jsonkey])
#             print(f"{self.version}{token}")
#         except FileNotFoundError:
#             print(f"Error: El archivo '{self.jsonfile}' no se encontró.")
#         except KeyError:
#             print(f"Error: La clave '{self.jsonkey}' no se encontró en el archivo JSON.")
#         except json.JSONDecodeError:
#             print(f"Error: El archivo '{self.jsonfile}' no contiene un JSON válido.")
#         except Exception as e:
#             print(f"Error: {str(e)}")

# def main():
#     if len(sys.argv) < 2 or sys.argv[1] == '-h':
#         extractor = TokenExtractor()
#         extractor.print_help()
#         return
    
#     if sys.argv[1] == '-v':
#         extractor = TokenExtractor()
#         extractor.print_version()
#         return

#     if len(sys.argv) < 3:
#         print("Error: Se esperaba al menos un argumento adicional.")
#         return

#     jsonfile = sys.argv[1]
#     jsonkey = sys.argv[2]

#     extractor = TokenExtractor(jsonfile, jsonkey)
#     extractor.extract_token()

# if __name__ == "__main__":
#     main()

#------------------Vercion ejercicio 4------------------
# #copyright UADER FCyT-IS2©2024 todos los derechos reservados

import json
import sys

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class TokenExtractor(metaclass=SingletonMeta):
    version = "1.2"

    def __init__(self, jsonfile="", jsonkey="token1"):
        self.jsonfile = jsonfile
        self.jsonkey = jsonkey

    def print_help(self):
        help_message = """
Extractor de token para acceso API Servicios Banco XXX (versión 1.2)

Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operará como un microservicio invocado mediante:

    {path ejecutable}/getJason.py {path archivo JSON}/{nombre archivo JSON}.json [clave]

ej.
    ./getJason.py ./sitedata.json token1

El token podrá recuperarse mediante el standard output de ejecución en el formato

    {1.2}XXXX-XXXX-XXXX-XXXX

Para obtener un mensaje de ayuda detallado ejecutar

    ./getJason.py -h

Excepciones

Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
terminar.
"""
        print(help_message)

    def extract_token(self):
        if len(sys.argv) < 2 or sys.argv[1] == '-h':
            self.print_help()
            return
        
        if sys.argv[1] == '-v':
            print(f"Versión del programa: {self.version}")
            return

        if len(sys.argv) < 3:
            print("Error: Se esperaba al menos un argumento adicional.")
            return

        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]

        try:
            with open(jsonfile, "r") as myfile:
                data = myfile.read()
            obj = json.loads(data)
            banks = obj.get("bancos", {})
            token = banks.get(jsonkey, {}).get("token", "")
            if token:
                print(f"{self.version}{token}")
            else:
                print(f"Error: La clave '{jsonkey}' no se encontró en el archivo JSON.")
        except FileNotFoundError:
            print(f"Error: El archivo '{jsonfile}' no se encontró.")
        except json.JSONDecodeError:
            print(f"Error: El archivo '{jsonfile}' no contiene un JSON válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    extractor = TokenExtractor()
    extractor.extract_token()