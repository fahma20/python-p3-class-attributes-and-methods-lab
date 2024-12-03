class Song:
    # Class attributes
    count = 0  # Keeps track of the number of songs
    genres = []  # List to store unique genres
    artists = []  # List to store unique artists
    genre_count = {}  # Dictionary to count songs per genre
    artist_count = {}  # Dictionary to count songs per artist

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        Song.add_song_to_count()

        # Add genre and artist to their respective lists and count them
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Add to genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the count of songs created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds unique genres to the genres list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds unique artists to the artists list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments the count of songs for each genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increments the count of songs for each artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


