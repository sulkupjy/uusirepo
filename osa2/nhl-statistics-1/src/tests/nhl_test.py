import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        self.joo = 3

    def test_testi(self):
        # Varmistetaan, että saldo on alussa 0
        self.assertAlmostEqual(self.joo, 3)
    def test_haku_onnistunut(self):
        # testataan haku
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")
    def test_haku_ei_onnistunut(self):
        #haku ei löydy testi
        pelaaja = self.stats.search("Jaahas")
        self.assertIsNone(pelaaja)
    def test_joukkueen_pelaajien_haku(self):
        #joukkueen pelaajien haku
        jpelaajat = self.stats.team("EDM")
        self.assertEqual(len(jpelaajat), 3
        )
    def test_parhaat_pelaajat(self):
        parhaat = self.stats.top(2)
        self.assertEqual(parhaat[0].name, "Gretzky")  
        self.assertEqual(parhaat[1].name, "Lemieux") 

