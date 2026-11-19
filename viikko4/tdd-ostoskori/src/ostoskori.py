from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._tavaroiden_maara = 0

    def tavaroita_korissa(self):
        return self._tavaroiden_maara

    def hinta(self):
        return 0

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroiden_maara += 1

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        pass
