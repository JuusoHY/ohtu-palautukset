
from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader


def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt")
    )

    print("Top point getters:")
    for player in stats.top(5, SortBy.POINTS):
        print(player)

    print("\nTop point getters (default):")
    for player in stats.top(5):
        print(player)

    print("\nTop goal scorers:")
    for player in stats.top(5, SortBy.GOALS):
        print(player)

    print("\nTop by assists:")
    for player in stats.top(5, SortBy.ASSISTS):
        print(player)


if __name__ == "__main__":
    main()
