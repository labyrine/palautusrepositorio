from urllib import request
from player import Player

class PlayerReader:
    def __init__(self, url_given):
        self._url = url_given

    def get_players(self):
        players_file = request.urlopen(self._url.get_url())
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
    
class GiveURL:
    def get_url(self):
        return "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    
class PlayerReaderIO:
    def __init__(self, url_giver):
        self._url_giver = url_giver

    def create(self):
        reader = PlayerReader(self._url_giver)
        return reader.get_players()

