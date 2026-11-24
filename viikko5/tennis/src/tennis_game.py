class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    POINT_LABELS = ("Love", "Fifteen", "Thirty", "Forty")

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self._equal_score()

        if self.player1_points >= 4 or self.player2_points >= 4:
            return self._endgame_score()

        return self._regular_score()

    def _equal_score(self):
        if self.player1_points >= 3:
            return "Deuce"

        return f"{self.POINT_LABELS[self.player1_points]}-All"

    def _endgame_score(self):
        difference = self.player1_points - self.player2_points
        leader = "player1" if difference > 0 else "player2"

        if abs(difference) == 1:
            return f"Advantage {leader}"

        return f"Win for {leader}"

    def _regular_score(self):
        first = self.POINT_LABELS[self.player1_points]
        second = self.POINT_LABELS[self.player2_points]

        return f"{first}-{second}"
