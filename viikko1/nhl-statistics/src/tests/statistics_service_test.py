
import unittest

from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytaa_pelaajan(self):
        self.assertEqual(
            self.stats.search("Gretzky").name,
            "Gretzky"
        )

    def test_search_loytaa_osittaisella_nimella(self):
        self.assertEqual(
            self.stats.search("Gret").name,
            "Gretzky"
        )

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        self.assertIsNone(self.stats.search("Messi"))

    def test_team_palauttaa_oikean_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [p.name for p in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_palauttaa_tyhjan_listan(self):
        self.assertEqual(self.stats.team("NYR"), [])

    def test_top_oletuksena_pisteiden_mukaan(self):
        self.assertEqual(
            [p.name for p in self.stats.top(5)],
            [
                "Gretzky",
                "Lemieux",
                "Yzerman",
                "Kurri",
                "Semenko"
            ]
        )

    def test_top_pisteiden_mukaan_enumilla(self):
        self.assertEqual(
            [p.name for p in self.stats.top(3, SortBy.POINTS)],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_maalien_mukaan(self):
        self.assertEqual(
            [p.name for p in self.stats.top(3, SortBy.GOALS)],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_syottojen_mukaan(self):
        self.assertEqual(
            [p.name for p in self.stats.top(3, SortBy.ASSISTS)],
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_palauttaa_vain_pyydetyn_maaran(self):
        self.assertEqual(len(self.stats.top(2)), 2)

    def test_top_liian_suuri_maara(self):
        self.assertEqual(len(self.stats.top(10)), 5)

    def test_top_nolla(self):
        self.assertEqual(self.stats.top(0), [])

    def test_top_negatiivinen(self):
        self.assertEqual(self.stats.top(-1), [])
