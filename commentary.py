'''
*Comentario (Commentary)
- id (id)
- id_usuario (id_user)
- id_cancion (id_song)
- fecha (date)
- descripcion (description)
'''

class Commentary:

    def __init__(self, id, id_user, id_song, date, description):
        self.id = id
        self.id_user = id_user
        self.id_song = id_song
        self.date = date
        self.description = description

    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # id_user
    def getId_user(self):
        return self.id_user
    
    def setId_user(self, id_user):
        self.id_user = id_user
    
    # id_song
    def getId_song(self):
        return self.id_song
    
    def setId_song(self, id_song):
        self.id_song = id_song

    # date
    def getDate(self):
        return self.date
    
    def setDate(self, date):
        self.date = date

    # description
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description