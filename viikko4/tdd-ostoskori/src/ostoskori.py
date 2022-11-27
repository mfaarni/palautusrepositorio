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
            hinta+=ostos.lukumaara()*ostos.hinta()
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
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
