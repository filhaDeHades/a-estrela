def obterDistancia(pos_grid_inicial, pos_grid_final, custo_menor_mov=1, custo_maior_mov=2):
    """Obtem a distância entre 2 células em um grid.

    Args:
        pos_grid_inicial (tuple): Posição no grid na qual deve se iniciar a contagem.
        pos_grid_final (tuple): Posição de destino no grid.
        custo_menor_mov (int, optional): Custo de movimentação nas direções
        ortogonal. Defaults to 1.
        custo_maior_mov (int, optional): Custo de movimentação nas
        diagonais. Defaults to 2.

    Returns:
        int: Valor da distância entre as 2 células inseridas na função.
    """

    dx = abs(pos_grid_final[0] - pos_grid_inicial[0])
    dy = abs(pos_grid_final[1] - pos_grid_inicial[1])

    if dx > dy:
        distancia = custo_maior_mov * dy + custo_menor_mov * (dx - dy)
    else:
        distancia = custo_maior_mov * dx + custo_menor_mov * (dy - dx)

    return distancia

def transformar_duas_listas_em_set(lista_1, lista_2):
    """Recebe 2 listas e as converte em um set.

    Args:
        lista_1 (list): Primeira lista que deve ser transformada em um set.
        lista_2 (list): Segunda lista que deve ser transformada em um set.

    Returns:
        set: Estrutura set resultante da união de duas listas.
    """

    set_1 = set(lista_1)
    set_2 = set(lista_2)
    set_final = set_1.union(set_2)
    return set_final