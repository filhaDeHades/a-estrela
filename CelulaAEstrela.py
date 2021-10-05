import funcoes_basicas as fb

class CelulaAEstrela:
    """Representa as células do grid e contém as funções
    necessárias para utilizar o algoritmo A*
    """

    def __init__(self, x, y, andavel=True, no_pai = None):
        self.g = 0
        self.h = 0
        self.f = 0
        self.grid_x = x
        self.grid_y = y
        self.pos_grid = (x, y)

        self.ja_foi_visitado = False
        self.ja_foi_analisado = False

        self.no_pai = no_pai
        self.andavel = andavel

    def addPai(self, no_pai):
        """Adiciona/atualiza a célula-pai na busca pelo menor caminho

        Args:
            no_pai (CelulaAEstrela): Célula anterior a célula atual no caminho
            até a célula destino.
        """

        self.noPai = no_pai

    def atualizarG(self):
        self.g = self.no_pai.g + fb.obterDistancia(self.no_pai.pos_grid, self.pos_grid)

    def atualizarH(self, pos_grid_final):
        self.h = fb.obterDistancia(self.pos_grid, pos_grid_final)

    def atualizarF(self):
        self.f = self.g + self.h