from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.build()
    print("Seuraavaksi pitäisi tulostua 958")
    filtered_with_all = stats.matches(matcher)
    print(len(filtered_with_all))

    print("Pelaaja, joiden joukkue on NYR")
    matcher = query.plays_in("NYR").build()

    for player in stats.matches(matcher):
        print(player)

    print("Pelaajat joiden joukkue on NYR, joilla on vähintään 10 mutta kuitenkin vähemmän kuin 20 maalia")
    matcher = (
      query
      .plays_in("NYR")
      .has_at_least(10, "goals")
      .has_fewer_than(20, "goals")
      .build()
    )

    for player in stats.matches(matcher):
        print(player)

    m1 = (
        query
            .plays_in("PHI")
            .has_at_least(10, "assists")
            .has_fewer_than(10, "goals")
            .build()
    )

    m2 = (
        query
            .plays_in("EDM")
            .has_at_least(50, "points")
            .build()
    )
    print("Or-ehdon sisältävä kysely")
    matcher = query.one_of(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)




if __name__ == "__main__":
    main()
