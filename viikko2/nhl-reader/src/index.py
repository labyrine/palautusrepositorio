import requests
from player import Player
from rich.console import Console
from rich.style import Style
from rich.prompt import Prompt
from rich.table import Table
console = Console()

def main():
    console.print("NHL statistics by nationality")
    season = Prompt.ask("Select season [magenta3][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/magenta3]")
    nationality = Prompt.ask("Select nationality [magenta3][AUT/CZE/AUS/SWE/GER/DEN/SUI/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/magenta3]")

    table = Table(title=f"Top scores of {nationality} season {season}")

    table.add_column("name", justify="left", style="cyan")
    table.add_column("team", justify="left", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality(nationality)

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console.print(table)

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players
    
class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scores_by_nationality(self, nationality):
        filtered_players = filter(lambda y: y.nationality == nationality, self.players)
        sorted_players = sorted(filtered_players, key=lambda x: x.points, reverse=True)
        
        return sorted_players
        
if __name__ == "__main__":
    main()
