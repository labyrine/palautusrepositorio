import unittest
from statistics_service import StatisticsService, SortBy
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
     
    def test_players_search_correct(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, "Kurri")

    def test_players_search_none(self):
        player = self.stats.search("Helloo")
        self.assertIsNone(player)

    def test_team_correct(self):
        team = self.stats.team("EDM")
        player_names = [player.name for player in team]
        self.assertEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_correct_default(self):
        top = self.stats.top(3)
        player_names = [player.name for player in top]
        self.assertEqual(player_names, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])

    def test_top_correct_points(self):
        top = self.stats.top(3, SortBy.POINTS)
        player_names = [player.name for player in top]
        self.assertEqual(player_names, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])

    def test_top_correct_goals(self):
        top = self.stats.top(3, SortBy.GOALS)
        player_names = [player.name for player in top]
        self.assertEqual(player_names, ["Lemieux", "Yzerman", "Kurri", "Gretzky"])

    def test_top_correct_assists(self):
        top = self.stats.top(3, SortBy.ASSISTS)
        player_names = [player.name for player in top]
        self.assertEqual(player_names, ["Gretzky", "Yzerman", "Lemieux", "Kurri"])

