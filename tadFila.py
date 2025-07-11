from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto

class Tipo(Enum):
    '''
    Classe para os tipos de atendimento
    '''
    GERAL = auto()
    PRIORITARIA = auto()

class Fila:
    '''
    Inicializa a fila por ordem de chegada garantindo os atendimentos gerais e prioritários
    Os atendimentos gerais podem ser ultrapassados até duas vezes e os prioritários ficam mais 
    a frente possível

    Exemplos:
    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira_geral()
    1
    >>> f.enfileira.geral()
    2
    >>> f.enfileira_prioridade()
    3
    >>> f.enfileira_prioridade()
    4
    >>> f.mostra_fila()
    '[3, 4, 1, 2]'
    >>> f.vazia()
    False
    >>> f.enfileira_geral()
    5
    >>> f.enfileira_prioridade()
    6
    >>> f.mostra_fila()
    '[3, 4, 1, 2, 6, 5]
    >>> f.desenfileira()
    3
    >>> f.mostra_fila
    '[4, 1, 2, 6, 5]'
    '''
    def __init__(self):
        '''
        Inicializa a fila de atendimento
        '''
        raise NotImplemented

    def enfileira_geral(self):
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
        raise NotImplemented

    def enfileira_prioritaria(self):
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
        >>> f.enfileira_prioridade()
        3
        >>> f.mostra_fila
        '[3, 1, 2]'
        '''
        raise NotImplemented

    def desenfileira(self):
        '''
        Remove a primeira demanda da fila e retorna o seu código.

        Exemplos:
        >>> f = Fila()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioridade()
        3
        >>> f.mostra_fila
        '[3, 1, 2]'
        >>> f.desenfileira()
        '[1, 2]'
        '''
        raise NotImplemented
    
    def mostra_fila(self):
        '''
        Mostra a fila de atendimento.
        
        Exemplos:
        >>> f = Fila()
        >>> f.enfileira_geral()
        1
        >>> f.enfileira_geral()
        2
        >>> f.enfileira_prioridade()
        3
        >>> f.mostra_fila()
        '[3, 1, 2]'
        '''
        raise NotImplemented

    def vazia(self):
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
        raise NotImplemented
