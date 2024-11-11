import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality("FIN")

    for player in players:
        print(player)

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
