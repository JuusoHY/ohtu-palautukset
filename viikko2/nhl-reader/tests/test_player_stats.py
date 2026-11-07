"""PlayerStats-luokan yksikkotestit."""

from player import Player
from player_stats import PlayerStats


class StubPlayerReader:
    """Palauttaa pelaajia ilman verkkoyhteytta."""

    def get_players(self):
        """Palauttaa testipelaajat."""
        return [
            Player({
                "name": "Pelaaja A",
                "team": "DAL",
                "nationality": "FIN",
                "goals": 10,
                "assists": 20,
            }),
            Player({
                "name": "Pelaaja B",
                "team": "COL, CAR, DAL",
                "nationality": "FIN",
                "goals": 20,
                "assists": 20,
            }),
            Player({
                "name": "Pelaaja C",
                "team": "CAR",
                "nationality": "SWE",
                "goals": 5,
                "assists": 10,
            }),
        ]


def test_nationality():
    """Testaa kansallisuussuodatuksen."""
    stats = PlayerStats(StubPlayerReader())
    players = stats.top_scorers_by_nationality("FIN")
    assert [p.name for p in players] == ["Pelaaja B", "Pelaaja A"]


def test_team():
    """Testaa joukkuesuodatuksen ja pistejarjestyksen."""
    stats = PlayerStats(StubPlayerReader())
    players = stats.top_scorers_by_team("DAL")
    assert [p.name for p in players] == ["Pelaaja B", "Pelaaja A"]


def test_team_lowercase():
    """Testaa pienilla kirjaimilla tehdyn haun."""
    stats = PlayerStats(StubPlayerReader())
    assert len(stats.top_scorers_by_team("dal")) == 2


def test_unknown_team():
    """Testaa tuntemattoman joukkueen."""
    stats = PlayerStats(StubPlayerReader())
    assert stats.top_scorers_by_team("XYZ") == []
