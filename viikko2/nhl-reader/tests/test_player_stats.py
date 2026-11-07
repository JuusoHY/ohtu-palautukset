"""Tests for PlayerStats."""

from player import Player
from player_stats import PlayerStats


class StubPlayerReader:
    """Returns predefined players without making an HTTP request."""

    def __init__(self, players):
        """Store the predefined player list."""
        self.players = players

    def get_players(self):
        """Return the predefined players."""
        return self.players


def create_player(data):
    """Create a Player instance from its input data."""
    return Player(data)


def create_stats():
    """Create stats with a fixed set of players."""
    players = [
        create_player({
            "name": "Alex", "team": "COL, CAR, DAL", "nationality": "CAN",
            "goals": 20, "assists": 30,
        }),
        create_player({
            "name": "Blake", "team": "COL", "nationality": "FIN",
            "goals": 10, "assists": 10,
        }),
        create_player({
            "name": "Casey", "team": "NYR", "nationality": "CAN",
            "goals": 30, "assists": 15,
        }),
    ]
    return PlayerStats(StubPlayerReader(players))


def test_top_scorers_by_nationality_returns_matching_players():
    """Filter players by nationality."""
    stats = create_stats()

    players = stats.top_scorers_by_nationality("CAN")

    assert [player.name for player in players] == ["Alex", "Casey"]


def test_top_scorers_by_team_returns_matching_players():
    """Return players who have played for the selected team."""
    stats = create_stats()

    players = stats.top_scorers_by_team("COL")

    assert [player.name for player in players] == ["Alex", "Blake"]


def test_top_scorers_by_team_sorts_by_points_descending():
    """Sort matching team players by points from highest to lowest."""
    stats = create_stats()

    players = stats.top_scorers_by_team("COL")

    assert [player.points for player in players] == [50, 20]


def test_top_scorers_by_team_matches_player_with_multiple_teams():
    """Match a team listed among several comma-separated teams."""
    stats = create_stats()

    players = stats.top_scorers_by_team("CAR")

    assert [player.name for player in players] == ["Alex"]
