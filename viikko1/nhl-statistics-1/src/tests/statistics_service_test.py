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
            PlayerReaderStub().get_players()
        )
     
    def test_players_search_correct(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, "Kurri")

    def test_players_search_none(self):
        player = self.stats.search("Helloo")
        self.assertIsNone(player)

    def test_team_correct(self):
        team = self.stats.team("EDM")
        player_names = [player.name for player in team]
        self.assertIn("Semenko", player_names)
        self.assertIn("Kurri", player_names)
        self.assertIn("Gretzky", player_names)

    def test_top_correct(self):
        top = self.stats.top(3)
        player_names = [player.name for player in top]
        self.assertIn("Gretzky", player_names[0])
        self.assertIn("Lemieux", player_names[1])
        self.assertIn("Yzerman", player_names[2])

