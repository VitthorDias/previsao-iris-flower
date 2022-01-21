import pandas as pd


class FlorSave:
    # Método para abrir o arquivo .csv
    @staticmethod
    def open():
        df = pd.read_csv("iris.csv")
        return df

    # Método para criar uma nova linha de dados para o .csv
    def create(self, new_iris):
        df = self.open()
        new_iris.iris_id = self.get_id()
        data = [new_iris.iris_id, new_iris.altura_sepala, new_iris.largura_sepala,
                new_iris.altura_petala, new_iris.largura_petala, new_iris.iris_flower]

        new_row = pd.DataFrame(data=[data], columns=df.columns)
        df = df.append(new_row)
        self.save(df)

    # Método para salvar o novo dataframe no .csv
    @staticmethod
    def save(df):
        df.to_csv("iris.csv", index=False)

    # Método para criar o id da nova flor
    @staticmethod
    def get_id():
        getid = pd.read_csv("iris.csv")

        if len(getid) == 0:
            return 1
        else:
            getid = getid.tail(1)
            getid = getid.id.values[0]
            return getid + 1
