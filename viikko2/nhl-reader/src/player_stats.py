"""Pelaajatilastojen suodatus ja jarjestaminen."""


class PlayerStats:
    """Kasittelee PlayerReaderin palauttamia pelaajia."""

    def __init__(self, reader):
        """Tallentaa pelaajien lukijan."""
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
        target_team = team.strip().upper()

        selected = [
            player for player in players
            if any(
                player_team.strip().upper() == target_team
                for player_team in player.team.split(",")
            )
        ]

        return sorted(
            selected,
            key=lambda player: player.points,
            reverse=True
        )
