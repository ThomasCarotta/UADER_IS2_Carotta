import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []  

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:  
            self.history.pop(0)

    def undo(self, num_states=1):
        if num_states > len(self.history):
            num_states = len(self.history)
        for _ in range(num_states):
            if self.history:
                memento = self.history.pop()
                self.file = memento.file
                self.content = memento.content
            else:
                print("No hay más estados anteriores para deshacer")

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, num_states=1):
        writer.undo(num_states)

if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("se invoca al <undo> una vez para recuperar el inmediato anterior")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> dos veces para recuperar los dos anteriores")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> tres veces para recuperar los tres anteriores")
    caretaker.undo(writer, 3)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> cuatro veces para recuperar los cuatro anteriores")
    caretaker.undo(writer, 4)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> una vez más para probar cuando no hay más estados")
    caretaker.undo(writer)