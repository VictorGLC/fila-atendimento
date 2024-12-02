from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy, copy
from fila_arranjo import  Tipo

class Pessoa:
    '''
    Estrutura inicial de uma pessoa na fila de atendimento
    '''
    ultrapassagens = int
    senha = int
    tipo = Tipo 
