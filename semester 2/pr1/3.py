class Musician:
    def __init__(self, name: str) -> None:
        self.name = name
        self.songlist = []
        self.albumlist = []
    def _add_song(self, song: 'Song') -> None:
        self.songlist.append(song)
        if not(song.album in self.albumlist):
            self.albumlist.append(song.album)

class Album:    
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year
        self.songlist = []
        self.musicianlist = []
    def _add_song(self, song: 'Song') -> None:
        self.songlist.append(song)
        if not(song.musician in self.musicianlist):
            self.musicianlist.append(song.musician)

class Song:
    def __init__(self, name: str, album: Album, *args: Musician) -> None:
        self.name = name
        self.musician = args
        self.album = album
        for singer in self.musician: singer._add_song(self)
        album._add_song(self)

class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.songdict = {}
        self.musiciandict = {}
    def add(self, song: Song) -> None:
        if not(song in self.songdict):
            self.songdict[f'{song.name}'] = song
            for singer in song.musician:
                if not(singer in self.musiciandict):
                    self.musiciandict[f'{singer.name}'] = 1
                else:
                    self.musiciandict[f'{singer.name}'] += 1
    def remove(self, song_name: str) -> None:
        # try:
            for singer in self.songdict[song_name].musician: 
                self.musiciandict[f'{singer.name}'] -= 1
                if self.musiciandict[f'{singer.name}'] == 0:
                    del self.musiciandict[f'{singer.name}']
            del self.songdict[song_name]
        # except:
        #     print(self.songdict[song_name].musician)
        
    def add_album(self, album: Album) -> None:
        for song in album.songlist:
            if not(song in self.songdict):
                self.songdict[f'{song.name}'] = song
                for singer in song.musician:
                    if not(singer in self.musiciandict):
                        self.musiciandict[f'{singer.name}'] = 1
                    else:
                        self.musiciandict[f'{singer.name}'] += 1

Ug = Album('Ugly is beautiful', 2020)
songs = [Song('Me, Myself & I', Ug, Musician('Oliver Tree')), Song('Jerk', Ug, Musician('Oliver Tree')),
         Song('J Song', Album('J Song', 2020), Musician('60 juno')), Song('MENTHOL*', Album('MENTHOL*', 2019), Musician('Jean Dawson'), Musician('Mac DeMarco'))]
morning = Playlist('Morning')
for song in songs:
    morning.add(song)
thedrums = Musician('The Drums')
portamento = Album('Portamento', 2011)
portamento_songs = ['Days', 'What You Were', 'Money']
for song in portamento_songs:
    Song(song, portamento, thedrums)
morning.add_album(portamento)
print(', '.join(morning.musiciandict.keys()))
print('; '.join(morning.songdict.keys()))
morning.remove('J Song')
print(', '.join(morning.musiciandict.keys()))
print('; '.join(morning.songdict.keys()))
