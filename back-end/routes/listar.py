from configs.config import *
from models.jogada import *


# curl localhost:5000/listar/Jogada
@app.route("/listar/<string:classe>")
def listar(classe):

    dados = None

    if classe == "Jogada":
        dados = db.session.query(Jogada).all()
        
    if dados:
        dados_json = []
        for d in dados:
            dados_json.append(d.json())

        dados_ordenados = sorted(dados_json, key=lambda d: d['tempo'])
        resposta = {"resultado": "ok", "detalhes": dados_ordenados}
        
    elif dados == []:
        resposta = jsonify({"resultado": "Erro!", "detalhes": " Sem dados"})
    
    else:
        resposta = jsonify({"resultado": "Erro!", "detalhes": "Classe informada inválida: "+classe})

    return resposta