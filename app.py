# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos
from user import User
from song import Song
from commentary import Commentary

app = Flask(__name__)

CORS(app)

# Declaracion de objetos
Users = []
Songs = []
Comments = []

# Datos ingresados
Users.append(User(1,'Angel', 'Ordon', 'root', 'root', 1))
Users.append(User(2,'Diego', 'Pinto', 'diego', '123', 2))

Songs.append(Song(1, 'International Love', 'Fidel Nadal', 'International Love', 'https://images-na.ssl-images-amazon.com/images/I/61AobF8AZLL._SY355_.jpg', '2008', 'https://open.spotify.com/track/2O282x8rik9PMihQAx6bAq?si=YBgZXzIzQoWI5b2x5Gzyqw', 'https://www.youtube.com/watch?v=y3WGp_ZEGUo', 1))
Songs.append(Song(2, 'Vibra Positiva', 'Zona Ganjah', 'Con Rastafari Todo Concuerda', 'https://i.scdn.co/image/ab67616d0000b273fb61203117d2324964d71c47', '2005', 'https://open.spotify.com/track/061cp08tzW2q8qaqNkad28?si=aXKtj4bvRhiANMoo7r3JRg', 'https://www.youtube.com/watch?v=lFw6sxMGIHk', 1))

Comments.append(Commentary(1, 1, 1, '2020', 'Que buena rola'))
Comments.append(Commentary(2, 2, 1, '2020', 'La escucho diario'))
Comments.append(Commentary(3, 1, 2, '2020', 'Me levanta el animo'))
Comments.append(Commentary(4, 2, 2, '2020', 'Buen ritmo'))

# --------------- INICIO RUTAS ---------------

@app.route('/', methods=['GET'])
def rutaInicial():
    return ("Corriendo API :D, uff")

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

    # obteniendo el ultimo id para tener un correlativo
    user = Users[-1]
    position = user.getId() + 1

    new = User(
        position,
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

# Obteniendo el ultimo registro de users
@app.route('/users/last', methods=['GET'])
def lastUser():
    global Users
    user = Users[-1]

    Fact = {
        'id': user.getId(),
        'name': user.getName(),
        'lastname': user.getLastname(),
        'username': user.getUsername(),
        'password': user.getPassword(),
        'user_type': user.getUser_type()
    }
    answer = jsonify({'message': 'Last user', 'user': Fact})
    return (answer)

# --------------- Song ---------------

# Get songs
@app.route('/songs', methods=['GET'])
def selectAllSongs():
    global Songs
    Data = []

    for song in Songs:
        Fact = {
            'id': song.getId(),
            'name': song.getName(),
            'artist': song.getArtist(),
            'album': song.getAlbum(),
            'image': song.getImage(),
            'date': song.getDate(),
            'link_spotify': song.getLink_spotify(),
            'link_youtube': song.getLink_youtube(),
            'state': song.getState()
        }
        Data.append(Fact)
    
    answer = jsonify({'songs': Data})

    return (answer)

# Get song
@app.route('/songs/<int:id>', methods=['GET'])
def findSong(id):
    global Songs
    for song in Songs:
        if song.getId() == id:
            Fact = {
                'id': song.getId(),
                'name': song.getName(),
                'artist': song.getArtist(),
                'album': song.getAlbum(),
                'image': song.getImage(),
                'date': song.getDate(),
                'link_spotify': song.getLink_spotify(),
                'link_youtube': song.getLink_youtube(),
                'state': song.getState()
            }
            break
    answer = jsonify({'message': 'Song found', 'song': Fact})
    return (answer)

# Post song
@app.route('/songs', methods=['POST'])
def insertSong():
    global Songs

    # obteniendo el ultimo id para tener un correlativo
    song = Songs[-1]
    position = song.getId() + 1

    new = Song(
        position,
        request.json['name'],
        request.json['artist'],
        request.json['album'],
        request.json['image'],
        request.json['date'],
        request.json['link_spotify'],
        request.json['link_youtube'],
        request.json['state']
    )
    Songs.append(new)
    answer = jsonify({'message': 'Added song'})
    return (answer)

# Put song
@app.route('/songs/<int:id>', methods=['PUT'])
def updateSong(id):
    global Songs
    for i in range(len(Songs)):
        if id == Songs[i].getId():
            Songs[i].setId(request.json['id'])
            Songs[i].setName(request.json['name'])
            Songs[i].setArtist(request.json['artist'])
            Songs[i].setAlbum(request.json['album'])
            Songs[i].setImage(request.json['image'])
            Songs[i].setDate(request.json['date'])
            Songs[i].setLink_spotify(request.json['link_spotify'])
            Songs[i].setLink_youtube(request.json['link_youtube'])
            Songs[i].setState(request.json['state'])
            break
    answer = jsonify({'message': 'Updated song'})
    return (answer)

# Delet song
@app.route('/songs/<int:id>', methods=['DELETE'])
def deleteSong(id):
    global Songs
    for i in range(len(Songs)):
        if id == Songs[i].getId():
            del Songs[i]
            break
    answer = jsonify({'message': 'Song Deleted'})
    return (answer)

# Obteniendo el ultimo registro de songs
@app.route('/songs/last', methods=['GET'])
def lastSong():
    global Songs
    song = Songs[-1]

    Fact = {
        'id': song.getId(),
        'name': song.getName(),
        'artist': song.getArtist(),
        'album': song.getAlbum(),
        'image': song.getImage(),
        'date': song.getDate(),
        'link_spotify': song.getLink_spotify(),
        'link_youtube': song.getLink_youtube(),
        'state': song.getState()
    }
    answer = jsonify({'message': 'Last song', 'song': Fact})
    return (answer)

# --------------- Commentary ---------------

# Get comments
@app.route('/comments', methods=['GET'])
def selectAllComments():
    global Comments
    Data = []

    for commentary in Comments:
        Fact = {
            'id': commentary.getId(),
            'id_user': commentary.getId_user(),
            'id_song': commentary.getId_song(),
            'date': commentary.getDate(),
            'description': commentary.getDescription()
        }
        Data.append(Fact)
    
    answer = jsonify({'comments': Data})

    return (answer)

# Get commentary
@app.route('/comments/<int:id>', methods=['GET'])
def findCommentary(id):
    global Comments
    for commentary in Comments:
        if commentary.getId() == id:
            Fact = {
                'id': commentary.getId(),
                'id_user': commentary.getId_user(),
                'id_song': commentary.getId_song(),
                'date': commentary.getDate(),
                'description': commentary.getDescription()
            }
            break
    answer = jsonify({'message': 'Commentary found', 'commentary': Fact})
    return (answer)

# Post commentary
@app.route('/comments', methods=['POST'])
def insertCommentary():
    global Comments

    # obteniendo el ultimo id para tener un correlativo
    commentary = Comments[-1]
    position = commentary.getId() + 1

    new = Commentary(
        position,
        request.json['id_user'],
        request.json['id_song'],
        request.json['date'],
        request.json['description']
    )
    Comments.append(new)
    answer = jsonify({'message': 'Added commentary'})
    return (answer)

# Put commentary
@app.route('/comments/<int:id>', methods=['PUT'])
def updateCommentary(id):
    global Comments
    for i in range(len(Comments)):
        if id == Comments[i].getId():
            Comments[i].setId(request.json['id'])
            Comments[i].setId_user(request.json['id_user'])
            Comments[i].setId_song(request.json['id_song'])
            Comments[i].setDate(request.json['date'])
            Comments[i].setDescription(request.json['description'])
            break
    answer = jsonify({'message': 'Updated commentary'})
    return (answer)

# Delet commentary
@app.route('/comments/<int:id>', methods=['DELETE'])
def deleteCommentary(id):
    global Comments
    for i in range(len(Comments)):
        if id == Comments[i].getId():
            del Comments[i]
            break
    answer = jsonify({'message': 'Commentary Deleted'})
    return (answer)

# Obteniendo el ultimo registro de comments
@app.route('/comments/last', methods=['GET'])
def lastCommentary():
    global Comments
    commentary = Comments[-1]

    Fact = {
        'id': commentary.getId(),
        'id_user': commentary.getId_user(),
        'id_song': commentary.getId_song(),
        'date': commentary.getDate(),
        'description': commentary.getDescription()
    }
    answer = jsonify({'message': 'Last commentary', 'commentary': Fact})
    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)