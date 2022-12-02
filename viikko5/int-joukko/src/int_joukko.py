KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):

        if n in self.lukujono:
                return True
        return False

    def lisaa(self, n):
        
        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lukumaara] = n
            self.alkioiden_lukumaara += 1

            if self.alkioiden_lukumaara == len(self.lukujono):
                for i in range(self.kasvatuskoko):
                    self.lukujono.append([0])


    def poista(self, numero):
        if numero in self.lukujono:
            self.lukujono.remove(numero)
            self.alkioiden_lukumaara-=1

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara

        for i in range(len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    def yhdiste(taulu_1, taulu_2):
        yhdistejoukko = IntJoukko()
        taulu_1 = taulu_1.to_int_list()
        taulu_2 = taulu_2.to_int_list()

        for i in range(len(taulu_1)):
            yhdistejoukko.lisaa(taulu_1[i])

        for i in range(len(taulu_2)):
            yhdistejoukko.lisaa(taulu_2[i])

        return yhdistejoukko

    def leikkaus(taulu_1, taulu_2):
        leikkausjoukko = IntJoukko()
        a_taulu = taulu_1.to_int_list()
        b_taulu = taulu_2.to_int_list()

        for alkio in a_taulu:
            if alkio in b_taulu:
                leikkausjoukko.lisaa(alkio)

        return leikkausjoukko

    def erotus(taulu_1, taulu_2):
        erotusjoukko = IntJoukko()
        a_taulu = taulu_1.to_int_list()
        b_taulu = taulu_2.to_int_list()

        for i in a_taulu:
            if i not in b_taulu:
                erotusjoukko.lisaa(i)

        return erotusjoukko

    def __str__(self):
        tuotos = ""
        if self.alkioiden_lukumaara>0:
            for i in range(self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
        return "{"+tuotos+"}"
