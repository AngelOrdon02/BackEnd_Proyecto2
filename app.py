# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos
from user import User

app = Flask(__name__)

CORS(app)

# Declaracion de objetos
Users = []

# Datos ingresados
Users.append(User(1,'Angel', 'Ordon', 'root', 'root', 1))
Users.append(User(2,'Diego', 'Pinto', 'diego', '123', 2))

# --------------- INICIO RUTAS ---------------

@app.route('/', methods=['GET'])
def rutaInicial():
    return ("Corriendo API :D, uff")

# Get users
@app.route('/users', methods=['GET'])
def selectAllUsers():
    global Users
    Data = []

    for user in Users:
        Fact = {
            'id': user.getId(),
            'name': user.getName(),
            'lastname': user.getLastname(),
            'username': user.getUsername(),
            'password': user.getPassword(),
            'user_type': user.getUser_type()
        }
        Data.append(Fact)
    
    answer = jsonify({'users': Data})

    return (answer)

# Get user
@app.route('/users/<int:id>', methods=['GET'])
def findUser(id):
    global Users
    for user in Users:
        if user.getId() == id:
            Fact = {
                'id': user.getId(),
                'name': user.getName(),
                'lastname': user.getLastname(),
                'username': user.getUsername(),
                'password': user.getPassword(),
                'user_type': user.getUser_type()
            }
            break
    answer = jsonify({'message': 'User found', 'user': Fact})
    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)