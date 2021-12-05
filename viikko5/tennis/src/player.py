class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def score(self):
        return self.score

    def name(self):
        return self.name

    def add_score(self):
        self.score = self.score + 1
