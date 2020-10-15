# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos

app = Flask(__name__)

CORS(app)

# --------------- INICIO RUTAS ---------------

@app.route('/', methods=['GET'])
def rutaInicial():
    return ("Corriendo API :D, uff")

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)