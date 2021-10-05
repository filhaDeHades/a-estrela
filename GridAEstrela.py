from CelulaAEstrela import CelulaAEstrela
import numpy as np
import funcoes_basicas as fb

class GridAEstrela:
    """Classe que representa o grid, contém as células do mesmo e
    a função principal do A*.
    """

    def __init__(self, qnt_linhas, qnt_colunas, matriz_layout = None):
        self.qnt_linhas = qnt_linhas
        self.qnt_colunas = qnt_colunas

        self.array_celulas = []
        self.lista_fechada = []

        if matriz_layout is None:
            self.obterArrayCelulasGridManual()
        else:
            self.obterArrayCelulasGridDefinido(matriz_layout)


    def obterArrayCelulasGridManual(self):
        """Cria um grid com células genéricas.
        """

        lista_celulas_temp = []

        for y in range(self.qnt_linhas):
            for x in range(self.qnt_colunas):
                nova_celula = CelulaAEstrela(x, y)
                lista_celulas_temp.append(nova_celula)

        array_final = np.array(lista_celulas_temp)
        self.array_celulas_grid = array_final


    # Não será utilizado no momento (possivelmente para visualização 2D)
    def obterArrayCelulasGridDefinido(self, layout):
        """Cria um grid com o layout definido ao instanciar o grid.

        Args:
            layout (list): Layout a ser definido.
        """
    
        lista_celulas_temp = []

        for y in range(self.qnt_linhas):
            for x in range(self.qnt_colunas):

                if layout[y][x] == 1: # É LUGAR
                    nova_celula = CelulaAEstrela(x, y, andavel=False)
                    lista_celulas_temp.append(nova_celula)
                else: # É ESPAÇO VAZIO
                    nova_celula = CelulaAEstrela(x, y, andavel=True)
                    lista_celulas_temp.append(nova_celula)

        array_final = np.array(lista_celulas_temp)

        self.array_celulas = array_final
    

    def obterCelulaArrayGrid(self, x, y):
        """Retorna a célula do array na posição determinada.

        Args:
            x (int): Posição na x da célula na matriz.
            y (int): Posição na y da célula na matriz.

        Returns:
            [CelulaAEstrela]: Célula na posição inserida na função.
        """

        pos_array = y * self.qnt_colunas + x
        celula = self.array_celulas[pos_array]
        return celula
    

    def obterNodulosVizinhos(self, celula, excluir_obstaculos=True, excluir_diagonais=False):
        """Obtem as células vizinhas a célula atual.

        Args:
            celula (CelulaAEstrela): Célula atual.
            excluir_obstaculos (bool, optional): Desconsidera qualquer
            obstáculo no caminho. Defaults to True.
            excluir_diagonais (bool, optional): Desconsidera qualquer
            diagonal para encontrar o caminho. Defaults to False.

        Returns:
            list: Lista contendo todos os vizinhos da célula atual.
        """

        lista_vizinhos = []

        for y in range(-1, 2):
            for x in range(-1, 2):

                if excluir_diagonais is True:
                    if abs(x) == 1 and abs(y) == 1:
                        continue

                pos_x = celula.grid_x + x
                pos_y = celula.grid_y + y

                if (pos_x, pos_y) == celula.pos_grid:
                    continue
                else:
                    if 0 <= pos_x <= self.qnt_colunas - 1:
                        if 0 <= pos_y <= self.qnt_linhas - 1:

                            celula_analisada = self.obterCelulaArrayGrid(pos_x, pos_y)

                            if excluir_obstaculos is True:
                                if celula_analisada.andavel is True:
                                    lista_vizinhos.append(celula_analisada)
                            else:
                                lista_vizinhos.append(celula_analisada)
        return lista_vizinhos
    

    def aEstrela(self, no1, no2):
        """Função principal do algoritmo A*.

        Args:
            no1 (CelulaAEstrela): Célula inicial.
            no2 (CelulaAEstrela): Célula de destino.

        Returns:
            [type]: [description]
        """

        custo_total = 0
        no1.g = 0
        no1.atualizarH(no2.pos_grid)
        no1.atualizarF()
        no1.ja_foi_visitado = True

        lista_aberta = []
        lista_fechada = []
        lista_aberta.append(no1)

        while len(lista_aberta) > 0:

            nodulo_atual = lista_aberta[0]  # obtendo o nodulo de menor f

            for nodulo in lista_aberta:
                if nodulo.f <= nodulo_atual.f and nodulo.h < nodulo_atual.h:
                    nodulo_atual = nodulo

            lista_aberta.remove(nodulo_atual)
            lista_fechada.append(nodulo_atual)

            if nodulo_atual == no2:

                lista_refinada = []

                nodulo_regresso = nodulo_atual

                while nodulo_regresso != no1:
                    lista_refinada.insert(0, nodulo_regresso.pos_grid)
                    nodulo_regresso = nodulo_regresso.no_pai

                lista_refinada.insert(0, no1.pos_grid)
                custo_total += no2.g

                lista_final = {"lista_refinada": lista_refinada}

                return custo_total

            lista_nodulos_vizinhos = self.obterNodulosVizinhos(nodulo_atual)

            for vizinho in lista_nodulos_vizinhos:

                if vizinho.ja_foi_visitado is False:
                    vizinho.no_pai = nodulo_atual
                    vizinho.atualizarG()
                    vizinho.atualizarH(no2.pos_grid)
                    vizinho.atualizarF()
                    vizinho.ja_foi_visitado = True

                if vizinho.andavel is False or vizinho in lista_fechada:
                    continue

                distacia_vizinho = fb.obterDistancia(nodulo_atual.pos_grid, vizinho.pos_grid)
                novo_mov_para_vizinho = nodulo_atual.g + distacia_vizinho

                if novo_mov_para_vizinho < vizinho.g or vizinho not in lista_aberta:
                    vizinho.g = novo_mov_para_vizinho
                    vizinho.atualizarF()
                    vizinho.parente = nodulo_atual
                    if vizinho not in lista_aberta:
                        lista_aberta.append(vizinho)
        return None
