from enum import Enum, auto
from copy import deepcopy

class Tipo(Enum):
    GERAL = auto()
    PRIORITARIA = auto()

class Demanda:
    def __init__(self, codigo: int, tipo: Tipo):
        self.codigo: int = codigo
        self.tipo: Tipo = tipo
        self.ultrapassagens: int = 2

class Fila:
    '''
    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira_geral()
    1
    >>> f.enfileira_geral()
    2
    >>> f.mostra_fila()
    '[1, 2]'
    >>> f.enfileira_prioridade()
    3
    >>> f.enfileira_prioridade()
    4
    >>> f.mostra_fila()
    '[3, 4, 1, 2]'
    >>> f.enfileira_geral()
    5
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 5]'
    >>> f.enfileira_prioridade()
    6
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 6, 5]'
    >>> f.enfileira_geral()
    7
    >>> f.enfileira_geral()
    8
    >>> f.enfileira_prioridade()
    9
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 6, 9, 5, 7, 8]'
    >>> f.desenfileira()
    3
    >>> f.desenfileira()
    4
    >>> f.mostra_fila()
    '[1, 2, 6, 9, 5, 7, 8]'
    >>> f.enfileira_prioridade()
    10
    >>> f.enfileira_prioridade()
    11
    >>> f.enfileira_prioridade()
    12
    >>> f.enfileira_prioridade()
    13
    >>> f.enfileira_geral()
    14
    >>> f.enfileira_geral()
    15
    >>> f.enfileira_prioridade()
    16
    >>> f.enfileira_prioridade()
    17
    >>> f.enfileira_prioridade()
    18
    >>> f.mostra_fila()
    '[1, 2, 6, 9, 5, 10, 7, 8, 11, 12, 13, 16, 17, 14, 15, 18]'
    '''
    def __init__(self):
        self.elementos: list[Demanda] = [Demanda(None, None)] * 8
        self.tam: int = 8
        self.fim: int = 0
        self.contador: int = 1

    def enfileira_geral(self) -> int:
        if self.tam - self.fim < 2:
            self.elementos = self.elementos + [Demanda(None, None)] * 5
            self.tam = len(self.elementos)

        self.elementos[self.fim] = deepcopy(Demanda(self.contador, Tipo.GERAL))
        self.contador+=1
        self.fim+=1
        return self.elementos[self.fim-1].codigo

    def enfileira_prioridade(self) -> int:
        if self.tam - self.fim < 2:
            self.elementos = self.elementos + [Demanda(None, None)] * 5
            self.tam = len(self.elementos)

        indice = self._encontra_indice()

        for i in range(self.fim, indice, -1):
            self.elementos[i] = self.elementos[i-1]

        self.elementos[indice] = deepcopy(Demanda(self.contador, Tipo.PRIORITARIA))
        self.contador+=1
        self.fim+=1

        return self.elementos[indice].codigo

    def mostra_fila(self) -> str:
        if self.vazia():
            return '[]'

        str = '['
        for i in range(self.fim-1):
            str += f'{self.elementos[i].codigo}, '
        str += f'{self.elementos[self.fim-1].codigo}]'

        return str
    
    def desenfileira(self) -> int:
        if self.vazia():
            raise ValueError('Fila vazia')
        
        primeira_demanda = self.elementos[0].codigo

        for i in range(1, self.fim):
            self.elementos[i-1] = self.elementos[i]

        self.fim-=1
 
        return primeira_demanda

    def vazia(self) -> bool:
        return self.fim == 0

    def _encontra_indice(self) -> int:

        for i in range(self.fim-1, 0, -1):
            demanda = self.elementos[i]

            if demanda.tipo == Tipo.PRIORITARIA:
                return i + 1

            elif demanda.tipo == Tipo.GERAL and demanda.ultrapassagens == 0:
                return i + 1

            elif demanda.tipo == Tipo.GERAL and demanda.ultrapassagens > 0:
                demanda.ultrapassagens -= 1

        if self.elementos[0].tipo == Tipo.PRIORITARIA:
            return 1
        else:
            self.elementos[0].ultrapassagens -= 1
            return 0