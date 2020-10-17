'''
*Lista de reproduccion (playlist)
- id (id)
- id_usuario (id_user)
- nombre (name)
- descripcion (description)
'''

class Playlist:
    
    def __init__(self, id, id_user, name, description):
        self.id = id
        self.id_user = id_user
        self.name = name
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
    
    # name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    # description
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description
    