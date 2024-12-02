from dataclasses import dataclass
from enum import Enum, auto

class Tipo(Enum):
    GERAL = auto()
    PRIORITARIA = auto()

class Demanda:
    def __init__(self, codigo: int, tipo: Tipo):
        self.codigo = codigo
        self.tipo = tipo
        self.ultrapassagens = 2

class Fila:
    def __init__(self):
        pass

    def enfileira_geral(self):
        raise NotImplemented

    def enfileira_prioridade(self):
        raise NotImplemented

    def mostra_fila(self):
        raise NotImplemented

    def vazia(self):
        raise NotImplemented