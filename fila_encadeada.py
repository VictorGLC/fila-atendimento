from __future__ import annotations
from dataclasses import dataclass
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
        self.ante: None # type: ignore
        self.prox: None # type: ignore

class Fila:
    sentinela: No
    contador: int
    
    def __init__(self):
        self.sentinela = No(None)
        self.sentinela.prox = self.sentinela
        self.sentinela.ante = self.sentinela
        self.contador = 0

    def enfileira_geral(self) -> int:
        self.contador += 1
        nova_demanda = deepcopy(No(Demanda(self.contador, 0, Tipo.Geral)))

        self.trata_enfileiramento(self.sentinela.ante, nova_demanda)

        return self.contador

    def enfileira_prioritaria(self) -> int:
        sentinela = self.sentinela.ante

        while sentinela.dado.tipo == Tipo.Geral and sentinela.item.ultrapassagens <2:
            sentinela.dado.ultrapassagens += 1
            sentinela = sentinela.ante

        self.contador += 1
        nova_demanda = deepcopy(No(Demanda(self.contador, 0, Tipo.Geral)))

        self.trata_enfileiramento(self.sentinela.ante, nova_demanda)

        return self.contador

    def trata_enfileiramento(self, sentinela: No, demanda: No):
        raise NotImplemented

    def vazia(self) -> bool:
        return self.sentinela.prox is self.sentinela

    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia.')
        
        rem = self.sentinela.prox.dado.codigo

        sentinela_AUX = self.sentinela.prox
        sentinela_AUX.prox.ante = sentinela_AUX.ante 
        sentinela_AUX.ante.prox = sentinela_AUX.prox

        return rem

    def mostra_fila(self) -> str:
        raise NotImplemented
