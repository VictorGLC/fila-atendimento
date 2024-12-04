from enum import Enum, auto

class Tipo(Enum):
    GERAL = auto()
    PRIORITARIA = auto()

class Demanda:
    def __init__(self, codigo: int, tipo: Tipo):
        self.codigo: int = codigo
        self.tipo: Tipo = tipo
        self.ultrapassagens: int = 2

class No:
    def __init__(self, demanda: Demanda):
        self.dado: Demanda = demanda
        self.ante: No | None = None
        self.prox: No | None = None

class Fila:
    def __init__(self):
        pass

    def enfileira_geral(self) -> int:
        raise NotImplemented

    def enfileira_prioridade(self) -> int:
        raise NotImplemented

    def mostra_fila(self) -> str:
        raise NotImplemented

    def vazia(self) -> bool:
        raise NotImplemented