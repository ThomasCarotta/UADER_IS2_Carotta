import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        station = self.stations[self.pos]
        if station in self.radio.memories[self.name].values():
            key = next(key for key, value in self.radio.memories[self.name].items() if value == station)
            print("Sintonizando... Frecuencia memorizada {} en memoria {} {}".format(station, key, self.name))
        else:
            print("Sintonizando... Estación {} {}".format(station, self.name))

class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510", "1450"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9", "92.3"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

        # Diccionario para almacenar las frecuencias memorizadas
        self.memories = {"AM": {"M1": "1250", "M2": "1380", "M3": "1510","M4":"1450"},
                        "FM": {"M1": "81.3", "M2": "89.1", "M3": "103.9","M4": "92.3"}}

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 4
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()

