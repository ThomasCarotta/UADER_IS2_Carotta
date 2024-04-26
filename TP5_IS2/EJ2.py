from collections.abc import Iterable, Iterator
from typing import Any


class CharIterator(Iterator):
    def __init__(self, string: str, reverse: bool = False):
        self._string = string
        self._reverse = reverse
        self._position = len(string) - 1 if reverse else 0
        self._step = -1 if reverse else 1

    def __next__(self) -> str:
        try:
            char = self._string[self._position]
            self._position += self._step
        except IndexError:
            raise StopIteration
        return char


class CharCollection(Iterable):
    def __init__(self, string: str):
        self._string = string

    def __iter__(self) -> CharIterator:
        return CharIterator(self._string)

    def get_reverse_iterator(self) -> CharIterator:
        return CharIterator(self._string, reverse=True)


if __name__ == "__main__":
    string = "Hello, world!"
    collection = CharCollection(string)

    print("Forward traversal:")
    forward_iterator = iter(collection)
    for char in forward_iterator:
        print(char, end="")
    print("\n")

    print("Reverse traversal:")
    reverse_iterator = collection.get_reverse_iterator()
    for char in reverse_iterator:
        print(char, end="")
