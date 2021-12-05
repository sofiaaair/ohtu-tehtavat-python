from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.players = [self.player1, self.player2]
        self.score = ""

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.add_score()
        else:
            self.player2.add_score()

    def get_score(self):
        temp_score = 0
        if self.player1.score == self.player2.score:
            self.points_are_even()

        elif self.player1.score >= 4 or self.player2.score >= 4:
            self.points_are_more_than_four()
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.score
                else:
                    self.score = self.score + "-"
                    temp_score = self.player2.score

                if temp_score == 0:
                    self.score = self.score + "Love"
                elif temp_score == 1:
                    self.score = self.score + "Fifteen"
                elif temp_score == 2:
                    self.score = self.score + "Thirty"
                elif temp_score == 3:
                    self.score = self.score + "Forty"

        return self.score

    def points_are_even(self):
            if self.player1.score == 0:
                self.score = "Love-All"
            elif self.player1.score == 1:
                self.score = "Fifteen-All"
            elif self.player1.score == 2:
                self.score = "Thirty-All"
            elif self.player1.score == 3:
                self.score = "Forty-All"
            else:
                self.score = "Deuce"

    def points_are_more_than_four(self):
        minus_result = self.player1.score - self.player2.score

        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"


