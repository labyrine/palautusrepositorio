KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti kasvatuskoossa")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujen_jono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.lukujen_jono[i]:
                return True
        return False
        
    def kasvata_taulukkoa(self):
        taulukko_vanha = self.lukujen_jono[:]
        uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
        self.lukujen_jono = self._luo_lista(uusi_koko)
        self.lukujen_jono[:len(taulukko_vanha)] = taulukko_vanha

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujen_jono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluu(n):
            self.lukujen_jono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lukujen_jono) == 0:
                self.kasvata_taulukkoa()

            return True

        return False
    
    def etsi_indeksi(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujen_jono[i]:
                return i
        return -1

    def poista(self, n):
        kohta = self.etsi_indeksi(n)

        if kohta != -1:
            for i in range(kohta, self.alkioiden_lkm - 1):
                self.lukujen_jono[i] = self.lukujen_jono[i + 1]

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujen_jono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for n in a_taulu + b_taulu:
            x.lisaa(n)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for n in a_taulu:
            if n in b_taulu:
                y.lisaa(n)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for n in a_taulu:
            if n not in b_taulu:
                z.lisaa(n)

        return z

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
