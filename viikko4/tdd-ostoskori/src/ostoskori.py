from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):

        tavarat=0
        for ostos in self.ostokset:
            tavarat+=ostos.lukumaara()
        return tavarat

    def hinta(self):

        hinta=0
        for ostos in self.ostokset:
            hinta+=ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        tuote = Ostos(lisattava)
        löytyy = False
        for ostos in self.ostokset:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                löytyy = True
        if not löytyy:
            self.ostokset.append(tuote)

    def poista_tuote(self, poistettava: Tuote):
        tuote = Ostos(poistettava)
        for ostos in self.ostokset:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                if ostos.lukumaara()>1:
                    ostos.muuta_lukumaaraa(-1)
                else:
                    self.ostokset.remove(ostos)

    def tyhjenna(self):
        self.ostokset.clear()

    def ostokset(self):
        return self.ostokset