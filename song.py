'''
*song
- id (id)
- nombre (name)
- artista (artist)
- album (album)
- imagen (image)
- fecha (date)
- link spotify (link_spotify)
- link youtube (link_youtube)
- estado (state)
'''

class Song:

    def __init__(self, id, name, artist, album, image, date, link_spotify, link_youtube, state):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.image = image
        self.date = date
        self.link_spotify = link_spotify
        self.link_youtube = link_youtube
        self.state = state
    
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
    
    # artist
    def getArtist(self):
        return self.artist
    
    def setArtist(self, artist):
        self.artist = artist
    
    # album
    def getAlbum(self):
        return self.album
    
    def setAlbum(self, album):
        self.album = album

    # image
    def getImage(self):
        return self.image
    
    def setImage(self, image):
        self.image = image

    # date
    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    # link_spotify
    def getLink_spotify(self):
        return self.link_spotify
    
    def setLink_spotify(self, link_spotify):
        self.link_spotify = link_spotify
    
    # link_youtube
    def getLink_youtube(self):
        return self.link_youtube
    
    def setLink_youtube(self, link_youtube):
        self.link_youtube = link_youtube
    
    # state
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
        