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
    >>> f.enfileira_prioritaria()
    3
    >>> f.mostra_fila()
    '[3, 1, 2]'
    >>> f.enfileira_prioritaria()
    4
    >>> f.mostra_fila()
    '[3, 4, 1, 2]'
    >>> f.enfileira_geral()
    5
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 5]'
    >>> f.enfileira_prioritaria()
    6
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 6, 5]'
    >>> f.enfileira_geral()
    7
    >>> f.enfileira_geral()
    8
    >>> f.enfileira_prioritaria()
    9
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 6, 9, 5, 7, 8]'
    >>> f.desenfileira()
    3
    >>> f.desenfileira()
    4
    >>> f.mostra_fila()
    '[1, 2, 6, 9, 5, 7, 8]'
    >>> f.enfileira_prioritaria()
    10
    >>> f.enfileira_prioritaria()
    11
    >>> f.enfileira_prioritaria()
    12
    >>> f.enfileira_prioritaria()
    13
    >>> f.enfileira_geral()
    14
    >>> f.enfileira_geral()
    15
    >>> f.enfileira_prioritaria()
    16
    >>> f.enfileira_prioritaria()
    17
    >>> f.enfileira_prioritaria()
    18
    >>> f.mostra_fila()
    '[1, 2, 6, 9, 5, 10, 7, 8, 11, 12, 13, 16, 17, 14, 15, 18]'

    >>> d = Fila()
    >>> d.enfileira_prioritaria()
    1
    >>> d.enfileira_prioritaria()
    2
    >>> d.enfileira_geral()
    3
    >>> d.enfileira_geral()
    4
    >>> d.mostra_fila()
    '[1, 2, 3, 4]'
    >>> d.desenfileira()
    1
    >>> d.desenfileira()
    2
    >>> d.desenfileira()
    3
    >>> d.desenfileira()
    4
    >>> d.vazia()
    True
    >>> d.enfileira_geral()
    5
    >>> d.vazia()
    False
    >>> d.enfileira_prioritaria()
    6
    >>> d.enfileira_prioritaria()
    7
    >>> d.enfileira_prioritaria()
    8
    >>> d.mostra_fila()
    '[6, 7, 5, 8]'

    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira_prioritaria()
    1
    >>> f.enfileira_geral()
    2
    >>> f.enfileira_geral()
    3
    >>> f.mostra_fila()
    '[1, 2, 3]'
    >>> f.enfileira_prioritaria()
    4
    >>> f.mostra_fila()
    '[1, 4, 2, 3]'
    >>> f.enfileira_geral()
    5
    >>> f.mostra_fila()
    '[1, 4, 2, 3, 5]'
    >>> f.enfileira_prioritaria()
    6
    >>> f.mostra_fila()
    '[1, 4, 6, 2, 3, 5]'
    >>> f.desenfileira()
    1
    >>> f.mostra_fila()
    '[4, 6, 2, 3, 5]'
    >>> f.enfileira_prioritaria()
    7
    >>> f.mostra_fila()
    '[4, 6, 2, 3, 7, 5]'
    >>> f.enfileira_prioritaria()
    8
    >>> f.enfileira_geral()
    9
    >>> f.mostra_fila()
    '[4, 6, 2, 3, 7, 5, 8, 9]'
    >>> f.desenfileira()
    4
    >>> f.mostra_fila()
    '[6, 2, 3, 7, 5, 8, 9]'

    >>> h = Fila()
    >>> h.enfileira_geral()
    1
    >>> h.enfileira_prioritaria()
    2
    >>> h.enfileira_geral()
    3
    >>> h.enfileira_geral()
    4
    >>> h.enfileira_prioritaria()
    5
    >>> h.mostra_fila()
    '[2, 5, 1, 3, 4]'
    >>> h.enfileira_geral()
    6
    >>> h.enfileira_geral()
    7
    >>> h.enfileira_prioritaria()
    8
    >>> h.mostra_fila()
    '[2, 5, 1, 8, 3, 4, 6, 7]'
    >>> h.enfileira_prioritaria()
    9
    >>> h.mostra_fila
    '[2, 5, 1, 8, 3, 4, 9, 6, 7]'
    '''
    def __init__(self):
        '''
        Inicializa a fila de atendimento.
        '''
        self.elementos: list[Demanda] = [Demanda(None, None)] * 8
        self.tam: int = 8
        self.fim: int = 0
        self.contador: int = 1

    def enfileira_geral(self) -> int:
        '''
        Insere o código de atendimento de tipo GERAL no final da fila e retorna o código atribuído sequencialmente.
        
        Exemplos:
        >>> f = Fila()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_geral()
        3
        '''
        if self.tam - self.fim < 2:
            self.elementos = self.elementos + [Demanda(None, None)] * 5
            self.tam = len(self.elementos)

        self.elementos[self.fim] = deepcopy(Demanda(self.contador, Tipo.GERAL))
        self.contador+=1
        self.fim+=1
        return self.elementos[self.fim-1].codigo

    def enfileira_prioritaria(self) -> int:
        '''
        Insere uma nova demanda do tipo PRIORITÁRIA na fila.
        Ela deve ser inserida antes de qualquer demanda PRIORITÁRIA ou antes de uma demanda GERAL com ultrapassagens igual a 0.
        Durante o processo, ultrapassagens das demandas gerais ultrapassadas são decrementadas.
        
        Exemplos:
        >>> f = Fila()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioritaria()
        3
        >>> f.mostra_fila()
        '[3, 1, 2]'
        '''
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
        '''
        Imprime a fila de atendimentos conforme a ordem de prioridade.
        
        Exemplos:
        >>> f = Fila()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioritaria()
        3
        >>> f.mostra_fila()
        '[3, 1, 2]'
        '''
        if self.vazia():
            return '[]'

        str = '['
        for i in range(self.fim-1):
            str += f'{self.elementos[i].codigo}, '
        str += f'{self.elementos[self.fim-1].codigo}]'

        return str
    
    def desenfileira(self) -> int:
        '''
        Remove a primeira demanda da fila e retorna o seu código.

        Exemplos:
        >>> f = Fila()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioritaria()
        3
        >>> f.mostra_fila()
        '[3, 1, 2]'
        >>> f.desenfileira()
        3
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        
        primeira_demanda = self.elementos[0].codigo

        for i in range(1, self.fim):
            self.elementos[i-1] = self.elementos[i]

        self.fim-=1
 
        return primeira_demanda

    def vazia(self) -> bool:
        '''
        Retorna True se a fila estiver vazia, e False caso contrário.

        Exemplos:
        >>> f = Fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        1
        >>> f.vazia()
        False
        '''
        return self.fim == 0

    def _encontra_indice(self) -> int:
        '''
        Busca de trás para frente e retorna o indice da posição que deve ser inserida uma nova demanda prioritária,
        ou seja, checa e retorna o indice anterior de uma demanda que é prioritária 
        ou do tipo geral que foi ultrapassada 2 vezes
        '''
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
