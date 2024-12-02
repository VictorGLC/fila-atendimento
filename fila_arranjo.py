from dataclasses import dataclass
from enum import Enum, auto

class Tipo(Enum):
    GERAL = auto()
    PRIORITARIA = auto()

class Item:
    def __init__(self, numero: int, nome: str, tipo: Tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.contador = 2

class Fila:
    def __init__(self):
        pass
