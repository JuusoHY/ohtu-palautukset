"""Pelaajien hakeminen HTTP-rajapinnasta."""

import requests

from player import Player


class PlayerReader:
    """Hakee rajapinnasta pelaajat Player-olioina."""

    def __init__(self, url):
        self.url = url

    def get_players(self):
        """Palauttaa rajapinnasta haetut pelaajat."""
        response = requests.get(self.url, timeout=15)
        response.raise_for_status()
        return [Player(data) for data in response.json()]
