import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    #määrä
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        olut = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(olut)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        olut = Tuote("Olut", 5)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    #hinta
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_paivittyy(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_paivittyy(self):
        maito = Tuote("Maito", 3)
        olut = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(olut)
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_paivittyy(self):
        olut = Tuote("Olut", 5)
        self.kori.lisaa_tuote(olut)
        self.kori.lisaa_tuote(olut)
        self.assertEqual(self.kori.hinta(), 10)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)


    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        olut = Tuote("Olut", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(olut)

        ostos1 = self.kori.ostokset[0]
        ostos2 = self.kori.ostokset[1]

        self.assertEqual(ostos1.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos1.lukumaara(), 1)
        self.assertEqual(ostos2.tuotteen_nimi(), "Olut")
        self.assertEqual(ostos2.lukumaara(), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset
        self.assertEqual(len(ostokset), 1)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jonka_lukumaara_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset[0]
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jonka_lukumaara_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset[0]
        self.assertEqual(ostos.lukumaara(), 1)


    def test_ainoan_lisatyn_tuotteen_poisto_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset
        self.assertEqual(len(ostokset),0)
        self.assertEqual(self.kori.hinta(),0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)



    def test_korin_tyhjennys(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset
        self.assertEqual(len(ostokset),1)
        self.kori.tyhjenna()
        self.assertEqual(len(ostokset),0)

