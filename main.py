import joblib
from flask import Flask
from flor import Flor
from save import FlorSave

flor = Flor()
flor_save = FlorSave()
app = Flask(__name__)
model_iris = joblib.load("iris_model.sav")


@app.route("/")
def hello():
    return "Bem vindo ao sistema de predição de classes Iris"


@app.route("/iris/predict/<alt_sepala>/<larg_sepala>/<alt_petala>/<larg_petala>/")
def iris_prediction(alt_sepala, larg_sepala, alt_petala, larg_petala):
    flor.altura_sepala = float(alt_sepala)
    flor.largura_sepala = float(larg_sepala)
    flor.altura_petala = float(alt_petala)
    flor.largura_petala = float(larg_petala)

    # Retorna se pelo menos um dos dados estiverem zerados ou negativos
    if not flor.validacao:
        return f"Predição não pode ser feita!!!"

    # Caso os dados estejam corretos, faz a predição e salva as informações no arquivo .csv
    dados = [[flor.altura_sepala, flor.largura_sepala, flor.altura_petala, flor.largura_petala]]

    flor.iris_flower = model_iris.predict(dados)[0]
    flor_save.create(flor)

    return f"Predição feita com sucesso!!!"


@app.route("/iris/result/")
def iris_result():
    flower = f"{flor.altura_sepala},{flor.largura_sepala},{flor.altura_petala},{flor.largura_petala},{flor.iris_flower}"
    return flower


app.run(host="192.168.1.64", port=8000)
