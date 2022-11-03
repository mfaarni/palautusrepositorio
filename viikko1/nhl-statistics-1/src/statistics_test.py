import unittest
from statistics import Statistics, SortBy
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
class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(
        PlayerReaderStub())



    def test_etsi_joukkueen_pelaajat(self):
        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux" )
    
    def test_etsi_parhaat_pelaajat_pisteillä(self):
        top_scorers = self.stats.top(4, SortBy.POINTS)
        self.assertEqual(top_scorers, self.stats.top(4, SortBy.POINTS)) 

    def test_etsi_parhaat_pelaajat_maaleilla(self):
        top_scorers = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(top_scorers, self.stats.top(4, SortBy.GOALS))

    def test_etsi_parhaat_pelaajat_avustuksilla(self):
        top_scorers = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(top_scorers, self.stats.top(4, SortBy.ASSISTS))

    def test_etsi_pelaaja(self):
        player=self.stats.search("Kurri").name
        self.assertEqual(player, "Kurri")

    def test_etsi_olematonta(self):
        player=self.stats.search("Miikkulainen")
        self.assertEqual(player, None)
