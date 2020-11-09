# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos
from user import User
from song import Song
from commentary import Commentary
from playlist import Playlist
from playlist_song import Playlist_song

app = Flask(__name__)

CORS(app)

# Declaracion de objetos
Users = []
Songs = []
Comments = []
Playlists = []
Playlist_song_array = []

# Datos ingresados
Users.append(User(1,'Angel', 'Ordon', 'root', 'root', 1))
Users.append(User(2,'Diego', 'Pinto', 'diego', '123', 2))

Songs.append(Song(1, 'International Love', 'Fidel Nadal', 'International Love', 'https://images-na.ssl-images-amazon.com/images/I/61AobF8AZLL._SY355_.jpg', '2008', 'https://open.spotify.com/embed/track/2O282x8rik9PMihQAx6bAq', 'https://www.youtube.com/embed/y3WGp_ZEGUo', 1))
Songs.append(Song(2, 'Vibra Positiva', 'Zona Ganjah', 'Con Rastafari Todo Concuerda', 'https://i.scdn.co/image/ab67616d0000b273fb61203117d2324964d71c47', '2005', 'https://open.spotify.com/embed/track/061cp08tzW2q8qaqNkad28', 'https://www.youtube.com/embed/lFw6sxMGIHk', 1))

Songs.append(Song(3, 'Vibra Positiva - inactiva', 'Zona Ganjah', 'Con Rastafari Todo Concuerda', 'https://i.scdn.co/image/ab67616d0000b273fb61203117d2324964d71c47', '2005', 'https://open.spotify.com/embed/track/061cp08tzW2q8qaqNkad28', 'https://www.youtube.com/embed/lFw6sxMGIHk', 2))
Songs.append(Song(4, 'Vibra Positiva - inactiva', 'Zona Ganjah', 'Con Rastafari Todo Concuerda', 'https://i.scdn.co/image/ab67616d0000b273fb61203117d2324964d71c47', '2005', 'https://open.spotify.com/embed/track/061cp08tzW2q8qaqNkad28', 'https://www.youtube.com/embed/lFw6sxMGIHk', 2))

Comments.append(Commentary(1, 1, 'root', 1, '2020', 'Que buena rola'))
Comments.append(Commentary(2, 2, 'diego', 1, '2020', 'La escucho diario'))
Comments.append(Commentary(3, 1, 'root', 2, '2020', 'Me levanta el animo'))
Comments.append(Commentary(4, 2, 'diego', 2, '2020', 'Buen ritmo'))

Playlists.append(Playlist(1, 1, 'Rolitas', 'Musica favorita :D'))
Playlists.append(Playlist(2, 2, 'Musica varia', 'Musica para el gimnasio'))

Playlist_song_array.append(Playlist_song(1, 1, 1))
Playlist_song_array.append(Playlist_song(2, 2, 1))
Playlist_song_array.append(Playlist_song(3, 1, 2))
Playlist_song_array.append(Playlist_song(4, 2, 2))

# --------------- CONTADORES ---------------
# Es cinco porque ya hay 4 registros en las lineas (29 - 33)
cont_song = 5

# --------------- INICIO RUTAS ---------------

@app.route('/', methods=['GET'])
def rutaInicial():
    #global cont_song
    return ("Corriendo API :D, uff: " + str(cont_song) + " hola")

# --------------- Auth ---------------

@app.route('/login', methods=['POST'])
def loginUser():
    global Users

    '''
    Si el state = 0 significa que hubo un error
    codigo cero (0) error

    Si el state = 1 significa que si se loggeo con exito
    codigo uno (1) username y password correctos

    Si el state = 2 significa que el password esta incorrecta
    codigo dos (2) username correcto y password incorrecto

    Si el state = 3 significa que el usuario esta incorrecto
    codigo tres (3) username incorrecto y password correcto

    Si el state = 4 significa que los datos son incorrectos
    codigo cuatro (4) username y password incorrectos
    '''

    username = request.json['username']
    password = request.json['password']
    id_user = 0

    state_username = False
    state_password = False
    state = 0

    for i in range(len(Users)):
        if username == Users[i].getUsername():
            state_username = True
            id_user = Users[i].getId()
            break
    
    for i in range(len(Users)):
        if password == Users[i].getPassword():
            state_password = True
            break
    
    if (state_username == False) and (state_password == False):
        state = 4
    elif (state_username == False) and (state_password == True):
        state = 3
    elif (state_username == True) and (state_password == False):
        state = 2
    elif (state_username == True) and (state_password == True):
        state = 1

    answer = jsonify({'message': 'Login process', 'state': state, 'id': id_user})
    return (answer)
    #answer = jsonify({'message': 'Added user'})
    #return (answer)

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
    #answer = jsonify(Data)

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

    # ------ Crea una playlist automatica por cada usuario ------
    global Playlists
    
    # obteniendo el ultimo id para tener un correlativo
    playlist = Playlists[-1]
    position_playlist = playlist.getId() + 1
    id_user = position
    
    name_user = request.json['username']
    name = "Playlist de " + str(name_user)
    description = "Playlist personal :D"

    new_playlist = Playlist(
        position_playlist,
        id_user,
        name,
        description
    )
    Playlists.append(new_playlist)
    
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

# Get user exists
@app.route('/user_exists/<string:username>', methods=['GET'])
def findUserExists(username):
    global Users

    '''
    Si el state = 0 significa que no existe ese usuario
    codigo cero (0) no existe

    Si el state = 1 significa que si existe ese usuario
    codigo uno (1) existe
    '''
    state = 0

    for i in range(len(Users)):
        if username == Users[i].getUsername():
            state = 1
            break
    
    if state == 1:
        answer = jsonify({'message': 'User exists', 'state': state})
        return (answer)
    elif state == 0:
        answer = jsonify({'message': 'User does not exist', 'state': state})
        return (answer)

# Get user - recover password
@app.route('/users_recover/<string:username>', methods=['GET'])
def recoverUser(username):
    global Users
    for user in Users:
        if user.getUsername() == username:
            password = user.getPassword()
            break
    answer = jsonify({'message': 'User found', 'user_password': password})
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
    
    #answer = jsonify(Data)
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
    #answer = jsonify(Fact)
    answer = jsonify({'message': 'Song found', 'song': Fact})
    return (answer)

# Post song
@app.route('/songs', methods=['POST'])
def insertSong():
    global Songs
    global cont_song

    # obteniendo el ultimo id para tener un correlativo
    #song = Songs[-1]
    #position = song.getId() + 1
    position = cont_song

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
    
    cont_song += 1
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

# Put song change state
@app.route('/songs_state/<int:id>', methods=['PUT'])
def updateSongState(id):
    global Songs
    for i in range(len(Songs)):
        if id == Songs[i].getId():
            Songs[i].setState(request.json['state'])
            break
    answer = jsonify({'message': 'Updated song_state'})
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
            'username_user': commentary.getUsername_user(),
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
                'username_user': commentary.getUsername_user(),
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
        request.json['username_user'],
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
            Comments[i].setUsername_user(request.json['username_user'])
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
        'username_user': commentary.getUsername_user(),
        'id_song': commentary.getId_song(),
        'date': commentary.getDate(),
        'description': commentary.getDescription()
    }
    answer = jsonify({'message': 'Last commentary', 'commentary': Fact})
    return (answer)

# Get comments for song
@app.route('/comments_song/<int:id>', methods=['GET'])
def selectAllCommentsSong(id):
    global Comments
    Data = []

    for commentary in Comments:
        if commentary.getId_song() == id:
            Fact = {
                'id': commentary.getId(),
                'id_user': commentary.getId_user(),
                'username_user': commentary.getUsername_user(),
                'id_song': commentary.getId_song(),
                'date': commentary.getDate(),
                'description': commentary.getDescription()
                }
            Data.append(Fact)
    
    answer = jsonify({'comments_song': Data})

    return (answer)

# --------------- Playlist ---------------

# Get playlists
@app.route('/playlists', methods=['GET'])
def selectAllPlaylists():
    global Playlists
    Data = []

    for playlist in Playlists:
        Fact = {
            'id': playlist.getId(),
            'id_user': playlist.getId_user(),
            'name': playlist.getName(),
            'description': playlist.getDescription()
        }
        Data.append(Fact)
    
    answer = jsonify({'playlists': Data})

    return (answer)

# Get playlist
@app.route('/playlists/<int:id>', methods=['GET'])
def findPlaylist(id):
    global Playlists
    for playlist in Playlists:
        if playlist.getId() == id:
            Fact = {
                'id': playlist.getId(),
                'id_user': playlist.getId_user(),
                'name': playlist.getName(),
                'description': playlist.getDescription()
            }
            break
    answer = jsonify({'message': 'Playlist found', 'playlist': Fact})
    return (answer)

# Post playlist
@app.route('/playlists', methods=['POST'])
def insertPlaylist():
    global Playlists

    # obteniendo el ultimo id para tener un correlativo
    playlist = Playlists[-1]
    position = playlist.getId() + 1

    new = Playlist(
        position,
        request.json['id_user'],
        request.json['name'],
        request.json['description']
    )
    Playlists.append(new)
    answer = jsonify({'message': 'Added playlist'})
    return (answer)

# Put playlist
@app.route('/playlists/<int:id>', methods=['PUT'])
def updatePlaylist(id):
    global Playlists
    for i in range(len(Playlists)):
        if id == Playlists[i].getId():
            Playlists[i].setId(request.json['id'])
            Playlists[i].setId_user(request.json['id_user'])
            Playlists[i].setName(request.json['name'])
            Playlists[i].setDescription(request.json['description'])
            break
    answer = jsonify({'message': 'Updated playlist'})
    return (answer)

# Delet playlist
@app.route('/playlists/<int:id>', methods=['DELETE'])
def deletePlaylist(id):
    global Playlists
    for i in range(len(Playlists)):
        if id == Playlists[i].getId():
            del Playlists[i]
            break
    answer = jsonify({'message': 'Playlist Deleted'})
    return (answer)

# Obteniendo el ultimo registro de playlists
@app.route('/playlists/last', methods=['GET'])
def lastPlaylist():
    global Playlists
    playlist = Playlists[-1]

    Fact = {
        'id': playlist.getId(),
        'id_user': playlist.getId_user(),
        'name': playlist.getName(),
        'description': playlist.getDescription()
    }
    answer = jsonify({'message': 'Last playlist', 'playlist': Fact})
    return (answer)

# --------------- Playlist_song ---------------

# Get playlist_song_array
@app.route('/playlist_song', methods=['GET'])
def selectAllPlaylist_song_array():
    global Playlist_song_array
    Data = []

    for playlist_song in Playlist_song_array:
        Fact = {
            'id': playlist_song.getId(),
            'id_playlist': playlist_song.getId_playlist(),
            'id_song': playlist_song.getId_song()
        }
        Data.append(Fact)
    
    answer = jsonify({'playlist_song_array': Data})

    return (answer)

# Get playlist_song
@app.route('/playlist_song/<int:id>', methods=['GET'])
def findPlaylist_song(id):
    global Playlist_song_array
    for playlist_song in Playlist_song_array:
        if playlist_song.getId() == id:
            Fact = {
                'id': playlist_song.getId(),
                'id_playlist': playlist_song.getId_playlist(),
                'id_song': playlist_song.getId_song()
            }
            break
    answer = jsonify({'message': 'Playlist_song found', 'playlist_song': Fact})
    return (answer)

# Post playlist_song
@app.route('/playlist_song', methods=['POST'])
def insertPlaylist_song():
    global Playlist_song_array

    # obteniendo el ultimo id para tener un correlativo
    playlist_song = Playlist_song_array[-1]
    position = playlist_song.getId() + 1

    new = Playlist_song(
        position,
        request.json['id_playlist'],
        request.json['id_song']
    )
    Playlist_song_array.append(new)
    answer = jsonify({'message': 'Added playlist_song'})
    return (answer)

# Put playlist_song
@app.route('/playlist_song/<int:id>', methods=['PUT'])
def updatePlaylist_song(id):
    global Playlist_song_array
    for i in range(len(Playlist_song_array)):
        if id == Playlist_song_array[i].getId():
            Playlist_song_array[i].setId(request.json['id'])
            Playlist_song_array[i].setId_playlist(request.json['id_playlist'])
            Playlist_song_array[i].setId_song(request.json['id_song'])
            break
    answer = jsonify({'message': 'Updated playlist_song'})
    return (answer)

# Delet playlist_song
@app.route('/playlist_song/<int:id>', methods=['DELETE'])
def deletePlaylist_song(id):
    global Playlist_song_array
    for i in range(len(Playlist_song_array)):
        if id == Playlist_song_array[i].getId():
            del Playlist_song_array[i]
            break
    answer = jsonify({'message': 'Playlist_song Deleted'})
    return (answer)

# Obteniendo el ultimo registro de playlist_song_array
@app.route('/playlist_song/last', methods=['GET'])
def lastPlaylist_song():
    global Playlist_song_array
    playlist_song = Playlist_song_array[-1]

    Fact = {
        'id': playlist_song.getId(),
        'id_playlist': playlist_song.getId_playlist(),
        'id_song': playlist_song.getId_song()
    }
    answer = jsonify({'message': 'Last playlist_song', 'playlist_song': Fact})
    return (answer)

# Get id_song exists in playlist_song_array
@app.route('/song_exists_playlist/<int:id>', methods=['GET'])
def findSongExistsPlaylist(id):
    global Playlist_song_array

    '''
    Si el state = 0 significa que no existe la cancion
    codigo cero (0) no existe

    Si el state = 1 significa que si existe la cancion
    codigo uno (1) existe
    '''
    state = 0

    for i in range(len(Playlist_song_array)):
        if id == Playlist_song_array[i].getId_song():
            state = 1
            break
    
    if state == 1:
        answer = jsonify({'message': 'Song exists', 'state': state})
        return (answer)
    elif state == 0:
        answer = jsonify({'message': 'Song does not exist', 'state': state})
        return (answer)

# Get playlist_song_array for id_playlist
@app.route('/playlist_song_id_playlist/<int:id>', methods=['GET'])
def selectAllPlaylist_song_array_idPlaylist(id):
    global Playlist_song_array
    Data = []

    for playlist_song in Playlist_song_array:
        if playlist_song.getId_playlist() == id:
            Fact = {
            'id': playlist_song.getId(),
            'id_playlist': playlist_song.getId_playlist(),
            'id_song': playlist_song.getId_song()
            }
            Data.append(Fact)
    
    answer = jsonify({'playlist_song_array_id_playlist': Data})

    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=3000, debug=True)
    app.run(threaded=True, host="0.0.0.0", port="5000", debug=True)