
import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        player = self.stats.search("Messi")

        self.assertIsNone(player)

    def test_search_loytaa_osittaisella_nimella(self):
        player = self.stats.search("Gret")

        self.assertEqual(player.name, "Gretzky")

    def test_team_palauttaa_oikean_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_team_palauttaa_tyhjan_listan(self):
        players = self.stats.team("NYR")

        self.assertEqual(players, [])

    def test_top_palauttaa_parhaat_pelaajat(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_palauttaa_oikean_jarjestyksen(self):
        players = self.stats.top(5)

        names = [player.name for player in players]

        self.assertEqual(
            names,
            [
                "Gretzky",
                "Lemieux",
                "Yzerman",
                "Kurri",
                "Semenko"
            ]
        )

    def test_top_liian_suuri_maara(self):
        players = self.stats.top(10)

        self.assertEqual(len(players), 5)

    def test_top_nolla_pelaajaa(self):
        players = self.stats.top(0)

        self.assertEqual(players, [])

    def test_top_negatiivinen_maara(self):
        players = self.stats.top(-1)

        self.assertEqual(players, [])
