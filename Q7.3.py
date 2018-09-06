class Song:
    def __init__(self, title, length, data):
        self.title = title
        self.length = length
        self.data = data
    def getData(self):
        return self.data

class CD:
    def __init__(self, title, songs, artist):
        self.title = title
        self.songs = songs
        self.artist  = artist
    def getSongs(self):
        return self.songs
    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist

class CDPlayer:
    def __init__(self):
        self.cd = None
    def insertCD(self, cd):
        self.cd = cd
    def ejectCD(self):
        if noEject:
            return
        cd = self.cd
        self.cd = None
        return cd
    def playCD(self):
        self.noEject = true
        for song in self.cd.getSongs():
            playSongFromData(song.getData())
        self.noEject = false


class JukeBox:
    def __init__(self):
        self.CDs = []
        self.CDPlayer = CDPlayer()

    def addCD(self, cd):
        self.CDs.append(cd)
    
    def playCD(self, cd):
        self.CDPlayer.insertCD(cd)
        self.CDPlayer.playCD()
        self.CDPlayer.ejectCD()
