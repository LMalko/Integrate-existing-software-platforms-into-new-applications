class Movie:

    def __init__(self, title, character_played, category, release_year):
        self.title = title
        self.character_played = character_played
        self.category = category
        self.release_year = release_year

    def __repr__(self):
        return f"{self.title} is a {self.category} released in {self.release_year} where"\
                     f" the actor played a role of {self.character_played}"