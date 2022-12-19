class Musik():
    def __init__(self, performer, song, album, year):
        self.performer=performer
        self.song=song
        self.album=album
        self.year=year

    def __str__(self):
        return 'Performer : ' +  self.performer +'\n'+'Song : ' + self.song +'\n'+'Album : ' + self.album +'\n'+'Year : ' + self.year  


musik= Musik("Ed Sheeran","Hearts Don't Break Around Here", "Divide", "2017")
print(musik)