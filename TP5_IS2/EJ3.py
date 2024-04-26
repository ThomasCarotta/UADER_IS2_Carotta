from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, id: str) -> None:
        pass


class ConcreteSubject(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Sujeto: Se adjuntó un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, id: str) -> None:
        print(f"\nSujeto: Notificando a los observadores para ID: {id}")
        for observer in self._observers:
            observer.update(id)


class Observer(ABC):
    @abstractmethod
    def update(self, id: str) -> None:
        pass


class ConcreteObserver(Observer):
    def __init__(self, observer_id: str):
        self._observer_id = observer_id

    def update(self, id: str) -> None:
        if id == self._observer_id:
            print(f"Observador {self._observer_id}: Recibió una notificación de ID coincidente")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_ids = ["ABCD", "EFGH", "IJKL", "MNOP"]
    observers = [ConcreteObserver(observer_id) for observer_id in observer_ids]

    for observer in observers:
        subject.attach(observer)

    emitted_ids = ["ABCD", "WXYZ", "IJKL", "MNOP", "EFGH", "QRST", "UVWX", "MNOP"]

    for id in emitted_ids:
        subject.notify(id)
