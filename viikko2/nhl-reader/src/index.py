"""NHL-pelaajien tilastot halutulta kaudelta."""

from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def show_players(players, nationality, season):
    """Tulostaa pelaajat taulukkona."""
    table = Table(title=f"{nationality} - {season}")

    table.add_column("Player")
    table.add_column("Team")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    Console().print(table)


def main():
    """Kaynnistaa sovelluksen."""
    country = input("Maa [FIN]: ").strip().upper() or "FIN"
    season = input("Kausi [2024-25]: ").strip() or "2024-25"

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    players = stats.top_scorers_by_nationality(country)

    show_players(players, country, season)


if __name__ == "__main__":
    main()
