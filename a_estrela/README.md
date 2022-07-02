# Algoritmo A* em um grid.

## Descrição:

Esse código implementa o algoritmo a* utilizando matrizes para simular grids.

Esse código foi criado para auxiliar no Projeto de Iniciação Científica que utiliza o repositório [Entropy](https://github.com/LucasMartelloNogueira/Entropy).

Esse diretório faz parte do repositório [satellite-code-entropy](https://github.com/filhaDeHades/satellite-code-entropy).

## Como o código funciona:
**1. A matriz**:

Suponha que temos uma matriz 4x4 representada abaixo onde "1" indicam os lugares ocupados e "0" indicam os lugares vazios.

    [0 1 0 0]
    [0 0 1 0]
    [1 0 0 1]
    [0 0 0 1]

Para utilizar essa matriz programa é necessário passar as seguintes informações:

- Posição de saída
- Posição de chegada
- Esse layout da matriz

Lembrando que as posições são indicadas por uma tupla em função de (i, j), onde "i" indica a qual linha pertence o lugar indicado e "j" representando qual a posição do lugar dentro da linha.

    OBS.: Caso você não esteja acostumado com a forma que a programação lida com listas, tuplas e dicionários; é importante que você saiba que a contagem começa do "0", logo, a primeira posição de uma array será a *posição 0* e assim por diante.

**Vamos escolher então 2 lugares para medir a distância: (0, 1) e (2, 3)**

Dessa forma a construção do programa ficaria assim:
```python
from AEstrela import a_estrela

matriz = [[0,1,0,0],[0,0,1,0],[1,0,0,1],[0,0,0,1]]

custoDeDeslocamento = a_estrela.aStar((0,1), (2,3), matriz)

```

## Unidade de Medida da Distância entre 2 células

## Como utilizar:
1. Adicionar a pasta "a_estrela" a raiz (root) do seu projeto/repositório.

2. Adicionar a linha a baixo no seu código.
```python
from AEstrela import a_estrela
```
3. Para utilizar a função basta escrever a linha abaixo no seu programa.
```python
custo = a_estrela.aStar(posicao1, posicao2, matriz)
```
A função retornará o a distância entre as 2 células.

## Autora:
[Tamires da Hora dos Santos](https://www.linkedin.com/in/tamires-da-hora-dos-santos-851a96170/)

Estudante de Ciência da Computação na UFF - (Universidade Federal Fluminense)