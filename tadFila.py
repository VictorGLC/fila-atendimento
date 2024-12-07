from __future__ import annotations

class Fila:
    def __init__(self):
        '''
        Inicializa a fila de atendimento.
        '''
        raise NotImplemented

    def enfileira_geral(self) -> int:
        '''
        Insere o código de atendimento de tipo GERAL no final da fila e retorna o código atribuído sequencialmente.
        '''
        raise NotImplemented

    def enfileira_prioritaria(self) -> int:
        '''
        Insere uma nova demanda do tipo PRIORITÁRIA na fila.
        Ela deve ser inserida antes de qualquer demanda PRIORITÁRIA ou antes de uma demanda GERAL com ultrapassagens igual a 0.
        Durante o processo, ultrapassagens das demandas gerais ultrapassadas são decrementadas.
        '''
        raise NotImplemented

    def mostra_fila(self) -> str:
        '''
        Imprime a fila de atendimentos conforme a ordem de prioridade.
        '''
        raise NotImplemented
    
    def desenfileira(self) -> int:
        '''
        Remove a primeira demanda da fila e retorna o seu código.
        '''
        raise NotImplemented

    def vazia(self) -> bool:
        '''
        Retorna True se a fila estiver vazia, e False caso contrário.
        '''
        raise NotImplemented
