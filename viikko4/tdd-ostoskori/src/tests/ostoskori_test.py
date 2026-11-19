import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_step_2_yhden_tuotteen_jalkeen_yksi_tavara(self):
        from tuote import Tuote
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_step_3_yhden_tuotteen_hinta(self):
        from tuote import Tuote
        maito = Tuote("Maito", 4)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 4)

    def test_step_4_kaksi_eri_tuotetta_maara(self):
        from tuote import Tuote
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_step_5_kahden_eri_tuotteen_hinta(self):
        from tuote import Tuote
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 8)

    def test_step_6_kaksi_samaa_tuotetta_maara(self):
        from tuote import Tuote
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_step_7_kahden_saman_tuotteen_hinta(self):
        from tuote import Tuote
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_step_8_lisays_tuottaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)
