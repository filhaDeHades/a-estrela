from GridAEstrela import GridAEstrela

def descobreTamanhoGrid(matriz):
    """Descobre o tamanho de uma matriz.

    Args:
        matriz (list): Matriz cujo tamanho deve ser descoberto.

    Returns:
        tuple: Tamanhos X e Y da matriz.
    """

    linhas = len(matriz)
    colunas = len(matriz[0])
    return (linhas, colunas)

def aStar(coord1, coord2, matriz):
    """Função de chamada do algoritmo A*.

    Args:
        coord1 (tuple): Primeira posição do grid cuja distância será calculada.
        coord2 (tuple): Segunda posição do grid cuja distância será calculada.
        matriz (list): Matriz a ser analisada.

    Returns:
        [type]: [description]
    """

    tam = descobreTamanhoGrid(matriz)
    grid = GridAEstrela(tam[0], tam[1], matriz)
    celula1 = grid.obterCelulaArrayGrid(coord1[0], coord1[1])
    celula2 = grid.obterCelulaArrayGrid(coord2[0], coord2[1])
    #print(f'celula1 array: {celula1.array_celulas_grid}\ncelula2 array: {celula2.array_celulas_grid}')
    return grid.aEstrela(celula1, celula2)
