'''Este módulo proporciona funciones para interactuar con el modelo de chatGPT.'''
import argparse #Se importa la libreria argparse
from openai import OpenAI #Se importa la libreria openai

# Inicialización del cliente de OpenAI

client=OpenAI(api_key=None) #Reemplazar None por la api Key

# Definición de variables de contexto y usuario
context = "Eres un astrónomo profesional"
usertask = "aprender"
userquery = "-"


ultimo_convers = []#Variable para almacenar la última consulta y respuesta

def procesar_consulta(consulta):
    '''Función que procesa la consulta'''
    try:
        # Tratamiento de consulta
        if consulta.strip():#elimina caracteres del principio y del final.
            print(f"You: {consulta}")
            # Invocación del modelo de OpenAI con la última consulta realizada
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {
                        "role": "system",
                        "content": context, 
                    },
                    {
                        "role": "user",
                        "content": usertask, #user task la dejo vacía porque no sé qué debería ir
                    },
                    {
                        "role": "user",
                        "content": consulta # consulta es la que ocupo principalmente
                    }
                ],
                temperature=1,
                max_tokens=150, # para limitar tokens y así ahorrar en la versión que tengo paga.
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            # Obtención de respuesta
            respuesta_chatgpt = response.choices[0].message.content #Finalmente captura la respuesta
            print(f"chatGPT: {respuesta_chatgpt}") # la devuelve
            # Agregar la consulta y la respuesta al buffer
            ultimo_convers.append((consulta, respuesta_chatgpt)) #se agrega a la lista

    except Exception as e: #Excepciones solicitadas y se declara en "e" para mayor facilidad
        print(f"Error en el procesamiento de la consulta: {e}") # se muestra por pantalla.


def manejar_eventos_teclado():
    '''Manejar eventos de teclas utilizando readline'''
    while True:
        entrada = input("")
        if entrada == "\x1b[A":  # "cursor Up"
            ultima_consulta = input("Ingrese su consulta (editar la última consulta): ")
            procesar_consulta(ultima_consulta) #se llama a procesar consulta nuevamente
        else:
            ultima_consulta = entrada
            procesar_consulta(entrada)


def modo_conversacion():
    '''Función para procesar el modo de conversación'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--convers", action="store_true", help="Modo de conversación")
    args = parser.parse_args()

    if args.convers:
        print("Modo de conversación activado. Presione Ctrl + C para salir.")
        manejar_eventos_teclado()
    else:
        print("El argumento '--convers' no está presente. Ignorando el modo de conversación.")


try:# Ejecutar el programa
    modo_conversacion()
except KeyboardInterrupt: #Una excepción fácil de probar
    print("\nSe ha interrumpido la ejecución del programa.")
