from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher1 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    print("Esimerkki")
    for player in stats.matches(matcher):
        print(player)

    print("NYR pelaajat, joilla ei ole vähintään kahta maalia")
    for player in stats.matches(matcher1):
        print(player)

    print("Seuraavaksi pitäisi tulostua 958")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("Or-luokan testaus")
    matcher2 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    for player in stats.matches(matcher2):
        print(player)
    
    print("Toinen esimerkki")
    matcher3 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher3):
        print(player)




if __name__ == "__main__":
    main()
