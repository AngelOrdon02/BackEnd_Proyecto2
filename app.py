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
    global Users
    #positon = Users[-1]
    #last_id = position.getId()

    user = Users[-1]

    Fact = {
        'id': user.getId(),
        'name': user.getName(),
        'lastname': user.getLastname(),
        'username': user.getUsername(),
        'password': user.getPassword(),
        'user_type': user.getUser_type()
    }

    answer = jsonify({'User': Fact})
    return (answer)
    #return ("Corriendo API :D, uff")

# --------------- User ---------------

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

# Post user
@app.route('/users', methods=['POST'])
def insertUser():
    global Users
    new = User(
        request.json['id'],
        request.json['name'],
        request.json['lastname'],
        request.json['username'],
        request.json['password'],
        request.json['user_type']
    )
    Users.append(new)
    answer = jsonify({'message': 'Added user'})
    return (answer)

# Put user
@app.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    global Users
    for i in range(len(Users)):
        if id == Users[i].getId():
            Users[i].setId(request.json['id'])
            Users[i].setName(request.json['name'])
            Users[i].setLastname(request.json['lastname'])
            Users[i].setUsername(request.json['username'])
            Users[i].setPassword(request.json['password'])
            Users[i].setUser_type(request.json['user_type'])
            break
    answer = jsonify({'message': 'Updated user'})
    return (answer)

# Delet user
@app.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    global Users
    for i in range(len(Users)):
        if id == Users[i].getId():
            del Users[i]
            break
    answer = jsonify({'message': 'User Deleted'})
    return (answer)


# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)