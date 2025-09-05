from abc import ABC, abstractmethod
import io
from typing import Iterator, Optional

# Component
class TextReader(ABC):
    """
    Clase abstracta que define la interfaz común para leer texto.
    """
    @abstractmethod
    def read(self, size: int = -1) -> str:
        pass
    @abstractmethod
    def close(self) -> None:
        pass


# ConcreteComponent

class FileTextReader(TextReader):
    """
    Envuelve un archivo de texto (o cualquier objeto compatible con .read/.close)
    sin agregar comportamiento extra.
    """
    def __init__(self, file_obj: io.TextIOBase):
        self._f = file_obj

    def read(self, size: int = -1) -> str:
        return self._f.read(size)

    def close(self) -> None:
        self._f.close()

# Decorator
class TextFilter(TextReader):
    """
    Decorador abstracto: mantiene una referencia a un TextReader y delega.
    Las subclases agregan responsabilidades (antes/después de delegar).
    """
    def __init__(self, wrapped: TextReader):
        self._wrapped = wrapped

    def read(self, size: int = -1) -> str:
        return self._wrapped.read(size)

    def close(self) -> None:
        self._wrapped.close()


# ConcreteDecorator (comportamiento 1)
class LowerCaseReader(TextFilter):
    """Convierte a minúsculas todo lo leído."""
    def read(self, size: int = -1) -> str:
        return super().read(size).lower()