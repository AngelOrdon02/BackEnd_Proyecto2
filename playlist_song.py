'''
*Lista de reproduccion - cancion (playlist_song)
- id (id)
- id_lista de reproduccion (id_playlist)
- id_cancion (id_song)
'''

class Playlist_song:

    def __init__(self, id, id_playlist, id_song):
        self.id = id
        self.id_playlist = id_playlist
        self.id_song = id_song
    
    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # id_playlist
    def getId_playlist(self):
        return self.id_playlist
    
    def setId_playlist(self, id_playlist):
        self.id_playlist = id_playlist

    # id_song
    def getId_song(self):
        return self.id_song
    
    def setId_song(self, id_song):
        self.id_song = id_song
    