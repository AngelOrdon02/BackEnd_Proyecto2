'''
*Usuario (User)
- id (id)
- nombre (name)
- apellido (lastname)
- nombre de usuario (username)
- contrasena (password)
- tipo_usuario (user_type)
'''

class User:

    def __init__(self, id, name, lastname, username, password, user_type):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.username = username
        self.password = password
        self.user_type = user_type

    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    # lastname
    def getLastname(self):
        return self.lastname
    
    def setLastname(self, lastname):
        self.lastname = lastname

    # username
    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        self.username = username

    # password
    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password

    # user_type
    def getUser_type(self):
        return self.user_type
    
    def setUser_type(self, user_type):
        self.user_type = user_type
    