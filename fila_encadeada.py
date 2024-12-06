from copy import deepcopy
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
    >>> f.mostra_fila()
    '[3, 1, 2]'
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

    >>> d = Fila()
    >>> d.enfileira_prioridade()
    1
    >>> d.enfileira_prioridade()
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
    >>> d.enfileira_prioridade()
    6
    >>> d.enfileira_prioridade()
    7
    >>> d.enfileira_prioridade()
    8
    >>> d.mostra_fila()
    '[6, 7, 5, 8]'

    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira_prioridade()
    1
    >>> f.enfileira_geral()
    2
    >>> f.enfileira_geral()
    3
    >>> f.mostra_fila()
    '[1, 2, 3]'
    >>> f.enfileira_prioridade()
    4
    >>> f.mostra_fila()
    '[1, 4, 2, 3]'
    >>> f.enfileira_geral()
    5
    >>> f.mostra_fila()
    '[1, 4, 2, 3, 5]'
    >>> f.enfileira_prioridade()
    6
    >>> f.mostra_fila()
    '[1, 4, 6, 2, 3, 5]'
    >>> f.desenfileira()
    1
    >>> f.mostra_fila()
    '[4, 6, 2, 3, 5]'
    >>> f.enfileira_prioridade()
    7
    >>> f.mostra_fila()
    '[4, 6, 2, 3, 7, 5]'
    >>> f.enfileira_prioridade()
    8
    >>> f.enfileira_geral()
    9
    >>> f.mostra_fila()
    '[4, 6, 2, 3, 7, 5, 8, 9]'
    >>> f.desenfileira()
    4
    >>> f.mostra_fila()
    '[6, 2, 3, 7, 5, 8, 9]'
    '''
    def __init__(self):
        '''
        Inicializa a fila de atendimento.
        '''
        self.primeiro = No(Demanda(None, None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ante = None
        self.contador = 1

    def enfileira_geral(self) -> int:
        '''
        Insere o código de atendimento de tipo GERAL no final da fila e retorna o código atribuído sequencialmente.
        '''
        nova_demanda = deepcopy(No(Demanda(self.contador, Tipo.GERAL)))
        self.contador+=1

        if self.vazia():
            self.primeiro.prox = nova_demanda
            nova_demanda.ante = self.primeiro
            self.ultimo = nova_demanda
            self.ultimo.ante = self.primeiro
            
            return nova_demanda.dado.codigo
        
        ptr = self.primeiro
        while ptr.prox != None:
            ptr = ptr.prox
        
        self.ultimo = nova_demanda
        self.ultimo.ante = ptr
        ptr.prox = self.ultimo

        return nova_demanda.dado.codigo
        
    def enfileira_prioridade(self) -> int:
        """
        Insere uma nova demanda do tipo PRIORITÁRIA na fila.
        Ela deve ser inserida antes de qualquer demanda PRIORITÁRIA ou antes de uma demanda GERAL com ultrapassagens igual a 0.
        Durante o processo, ultrapassagens das demandas gerais ultrapassadas são decrementadas.
        """
        # Criação de nova demanda prioritária
        nova_demanda = deepcopy(No(Demanda(self.contador, Tipo.PRIORITARIA)))
        self.contador += 1

        ptr = self.ultimo
        while ptr != self.primeiro and not (ptr.dado.tipo == Tipo.PRIORITARIA or (ptr.dado.tipo == Tipo.GERAL and ptr.dado.ultrapassagens == 0)):
            if ptr.dado.tipo == Tipo.GERAL and ptr.dado.ultrapassagens > 0:
                ptr.dado.ultrapassagens -= 1
            ptr = ptr.ante

        if ptr == self.primeiro:
            # Inserir no início da fila (após o nó fictício)
            nova_demanda.prox = self.primeiro.prox
            nova_demanda.ante = self.primeiro
            if self.primeiro.prox:
                self.primeiro.prox.ante = nova_demanda
            self.primeiro.prox = nova_demanda
            if self.ultimo == self.primeiro:  # Caso a fila esteja vazia
                self.ultimo = nova_demanda
        else:
            nova_demanda.prox = ptr.prox
            nova_demanda.ante = ptr
            if ptr.prox:
                ptr.prox.ante = nova_demanda
            ptr.prox = nova_demanda
            if ptr == self.ultimo:
                self.ultimo = nova_demanda

        return nova_demanda.dado.codigo

    def vazia(self) -> bool:
        return self.primeiro == self.ultimo

    def desenfileira(self):
        '''
        Remove a primeira demanda da fila e retorna o seu código.
        '''
        if self.vazia():
            raise ValueError('Fila vazia.')
        
        rem = self.primeiro.prox

        rem.ante = None
        self.primeiro.prox = rem.prox
        rem.prox = self.primeiro
        rem.prox = None

        if self.primeiro.prox == None:
            self.ultimo = self.primeiro

        return rem.dado.codigo

    def mostra_fila(self) -> str:
        '''
        Retorna True se a fila estiver vazia, e False caso contrário.
        '''
        if self.vazia():
            return '[]'
 
        str = "["
        ptr = self.primeiro.prox

        while ptr.prox != None:
            str+=f'{ptr.dado.codigo}, '
            ptr = ptr.prox

        str += f'{ptr.dado.codigo}]'
        return str