from configs.config import *
from models.jogada import *

# curl localhost:5000/incluir/Jogada -X POST -d '{"tempo": 10.5}' -H "Content-Type:application/json"
@app.route("/incluir/<string:classe>", methods=["post"])
def incluir(classe):
    dados = request.get_json()

    try:
        nova = None
        if classe == "Jogada":
            nova = Jogada(**dados)

        db.session.add(nova)
        db.session.commit()
        resposta = jsonify({"resultado": "Tempo adicionado!"})

    except Exception as error:
        resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    return resposta