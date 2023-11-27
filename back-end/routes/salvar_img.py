from configs.config import *

# curl -i -X POST -F files=@foto.jpeg localhost:5000/salvar_img
@app.route("/salvar_img", methods=["post"])
def salvar_img():

    try:
        file = request.files["imagem"]
        caminho_salvar = os.path.join(pastaimagem, 'background.png')
        file.save(caminho_salvar)
        resposta = jsonify({"resultado":"ok", "detalhes": "Imagem salva"})

    except Exception as erro:
        resposta = jsonify({"resposta": "Erro!", "detalhes": str(erro)})

    return resposta