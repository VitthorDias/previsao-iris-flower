class Flor:
    def __init__(self, alt_sepala=0, larg_sepala=0, alt_petala=0, larg_petala=0, classe=""):
        self._id = None
        self._alt_sepala = alt_sepala
        self._larg_sepala = larg_sepala
        self._alt_petala = alt_petala
        self._larg_petala = larg_petala
        self._iris_flower = classe
        self._validacao = True

    # Métodos de Altura da Sepala
    @property
    def altura_sepala(self):
        return self._alt_sepala

    @altura_sepala.setter
    def altura_sepala(self, value):
        value = float(value)

        if value > 0:
            self._alt_sepala = value
        elif self._validacao:
            self._validacao = False

    # Métodos de Largura da Sepala
    @property
    def largura_sepala(self):
        return self._larg_sepala

    @largura_sepala.setter
    def largura_sepala(self, value):
        value = float(value)

        if value > 0:
            self._larg_sepala = value
        elif self._validacao:
            self._validacao = False

    # Métodos de Altura da Petala
    @property
    def altura_petala(self):
        return self._alt_petala

    @altura_petala.setter
    def altura_petala(self, value):
        value = float(value)

        if value > 0:
            self._alt_petala = value
        else:
            self._validacao = False

    # Métodos de Largura da Petala
    @property
    def largura_petala(self):
        return self._larg_petala

    @largura_petala.setter
    def largura_petala(self, value):
        value = float(value)

        if value > 0:
            self._larg_petala = value
        else:
            self._validacao = False

    # Métodos da Predição da Iris
    @property
    def iris_flower(self):
        return self._iris_flower

    @iris_flower.setter
    def iris_flower(self, result):
        if result in ["SETOSA", "VERSICOLOR", "VIRGINICA"]:
            self._iris_flower = result

    # Método da validação dos dados inseridos
    @property
    def validacao(self):
        if not self._validacao:
            self._validacao = True
            return False
        else:
            return self._validacao

    # Métodos do id da flor
    @property
    def iris_id(self):
        return self._id

    @iris_id.setter
    def iris_id(self, new_id):
        self._id = new_id
