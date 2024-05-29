import json
import sys

class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        try:
            with open(self.file_path, "r") as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: No se encontro el archivo {self.file_path} .")
        except json.JSONDecodeError:
            raise ValueError("Error: El archivo no es un JSON válido.")

class TokenFormatter:
    def format_token(token):
        return f"{1.0}{token}"
class JSONParser:
    def parse_json(json_obj, key):
        try:
            return json_obj[key]
        except KeyError:
            raise KeyError(f"Error: La clave no se encontró en el archivo JSON: {key}.")

class Program:
    def __init__(self, json_reader, token_formatter, json_parser):
        self.json_reader = json_reader
        self.token_formatter = token_formatter
        self.json_parser = json_parser

    def run(self, json_key):
        try:
            json_obj = self.json_reader.read_json()
            value = self.json_parser.parse_json(json_obj, json_key)
            formatted_token = self.token_formatter.format_token(str(value))
            print(formatted_token)
        except Exception as e:
            print(f"Error inesperado: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] == '-h':
        print("Forma de usar el comando: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json {clave}")
        sys.exit(1)

    json_file = sys.argv[1]
    jsonkey = sys.argv[2]

    json_reader = JSONReader(json_file)
    token_formatter = TokenFormatter()
    json_parser = JSONParser()
    program = Program(json_reader, token_formatter, json_parser)
    program.run(jsonkey)
