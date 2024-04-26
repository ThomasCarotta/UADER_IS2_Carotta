from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class PrimeNumberHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        if self.is_prime(request):
            return f"{request} es un número primo"
        else:
            return super().handle(request)

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


class EvenNumberHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        if request % 2 == 0:
            return f"{request} es un número par"
        else:
            return super().handle(request)


class NumberProcessor:
    def __init__(self, handler: Handler):
        self._handler = handler

    def process_numbers(self, start: int, end: int):
        for num in range(start, end + 1):
            result = self._handler.handle(num)
            if result:
                print(result)
            else:
                print(f"{num} no fue consumido")


if __name__ == "__main__":
    prime_handler = PrimeNumberHandler()
    even_handler = EvenNumberHandler()

    prime_handler.set_next(even_handler)

    processor = NumberProcessor(prime_handler)
    processor.process_numbers(1, 100)