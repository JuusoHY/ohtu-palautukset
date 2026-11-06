"""NHL-pelaajaa kuvaava luokka."""


class Player:
    """Yksittaisen pelaajan tilastot."""

    def __init__(self, data):
        self.name = data["name"]
        self.team = data["team"]
        self.nationality = data["nationality"]
        self.goals = int(data["goals"])
        self.assists = int(data["assists"])

    @property
    def points(self):
        """Palauttaa pisteiden yhteismaaran."""
        return self.goals + self.assists

    def __str__(self):
        return (
            f"{self.name:22} {self.team:14} "
            f"{self.goals} + {self.assists} = {self.points}"
        )
