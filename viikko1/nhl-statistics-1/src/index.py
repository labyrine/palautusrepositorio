from statistics_service import StatisticsService, GiveURL, PlayerReaderIO


def main():
    url_giver = GiveURL()
    player_reader = PlayerReaderIO(url_giver)
    players = player_reader.create()
    stats = StatisticsService(players)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
