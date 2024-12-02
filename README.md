# Primeiro Trabalho - Fila de Atendimento

## 1. Objetivos

O objetivo do trabalho é avaliar a capacidade do aluno de:
- Especificar TADs
- Utilizar arranjos na implementação de TADs
- Utilizar encadeamento duplo na implementação de TADs

## 2. Instruções

- O trabalho é em equipe de até duas pessoas e deve ser entregue no Classroom até **às 23 horas e 59 minutos do dia anterior à prova** (que ainda será marcada).
- Cada aluno deve agendar a data da entrevista em uma planilha a ser disponibilizada.
- Trabalhos que não tenham sido feitos pela equipe em sua totalidade serão zerados.
- O ChatGPT e ferramentas similares **não podem fazer parte de nenhuma equipe!**

## 3. Descrição

Em um sistema de teleatendimento, uma única fila é usada para manter as demandas. Cada demanda gera um número sequencial, que é colocado na fila. Existem dois tipos de demanda: **geral** e **prioritária**, e embora o atendimento geral seja feito por ordem de chegada, as seguintes regras devem ser respeitadas:

- As demandas prioritárias ficam na frente das gerais.
- Cada demanda geral só pode ser "passada" por até **duas prioritárias**.

O exemplo a seguir demonstra o funcionamento de um TAD com esse comportamento:

```python
>>> f = fila()
>>> f.vazia()
True
>>> f.enfileira_geral()
1
>>> f.enfileira_geral()
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
'[3, 4, 1, 2, 6, 5]'
>>> f.desenfileira()
3
>>> f.mostra_fila()
'[4, 1, 2, 6, 5]'
```

## 4. Atividades

O trabalho consiste em:
- Fazer a especificação de um TAD para fila com o comportamento descrito.
- Implementar o TAD usando arranjos.
- Implementar o TAD usando encadeamento duplo.

**Nota**: A especificação do TAD deve conter os exemplos!

### Testando o Programa

Para verificar o funcionamento do seu programa, além dos exemplos do doctest, você deve usar o programa `trab1-teste.py` disponibilizado pelo professor. O programa lê um arquivo com as demandas em ordem de chegada e mostra na tela a ordem em que elas serão atendidas. 

Antes de executar o programa, você deve alterar a linha do `import` para importar a fila que você implementou. Depois disso, você pode executar o programa com o comando:

```bash
$ python3 trab1-teste.py arquivo.txt
```

### Exemplo de Entrada e Saída

Considerando um arquivo com o conteúdo (as linhas com asterisco são prioritárias):

```
João
Maria
* Pedro
* Paula
Ana
* Jorge
```

A saída do programa será:

```
3 Pedro
4 Paula
1 João
2 Maria
6 Jorge
5 Ana
```