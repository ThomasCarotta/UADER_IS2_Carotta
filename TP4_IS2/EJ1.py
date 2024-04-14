from ping3 import ping, verbose_ping
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def execute(self, ip: str) -> None:
        pass

class Ping(Subject):
    def execute(self, ip: str) -> None:
        if ip.startswith("192."):
            for _ in range(10):
                print(ping(ip))

    def executefree(self, ip: str) -> None:
        for _ in range(10):
            print(ping(ip))

class PingProxy(Subject):
    def __init__(self, real_subject: Ping) -> None:
        self._real_subject = real_subject

    def execute(self, ip: str) -> None:
        if ip == "192.168.0.254":
            self._real_subject.executefree("www.google.com")
        else:
            self._real_subject.execute(ip)

def client_code(subject: Subject, ip: str) -> None:
    subject.execute(ip)

if __name__ == "__main__":
    print("Client: Ejecutando el código del cliente con un sujeto real:")
    real_subject = Ping()
    client_code(real_subject, "192.168.1.1")

    print("")

    print("Client: Ejecutando el mismo código del cliente con un proxy:")
    proxy = PingProxy(real_subject)
    client_code(proxy, "192.168.0.254")