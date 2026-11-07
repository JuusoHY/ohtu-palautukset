"""Pelaajien tilastojen kasittely."""


class PlayerStats:
    """Muodostaa tilastoja PlayerReaderin pelaajista."""

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        """Palauttaa maan pelaajat pistejarjestyksessa."""
        players = self.reader.get_players()

        selected = [
            player for player in players
            if player.nationality == nationality.upper()
        ]

        return sorted(
            selected,
            key=lambda player: player.points,
            reverse=True
        )

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pistejarjestyksessa."""
        players = self.reader.get_players()
        selected = [
            player for player in players
            if team.upper() in [
                name.strip() for name in player.team.split(",")
            ]
        ]
        return sorted(
            selected,
            key=lambda player: player.points,
            reverse=True
        )
