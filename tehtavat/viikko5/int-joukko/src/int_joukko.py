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
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False


    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm == len(self.ljono):
            self.kasvata_listaa()

        self.ljono[self.alkioiden_lkm]=n            
        self.alkioiden_lkm +=1
        return True


    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                for j in range(i, self.alkioiden_lkm-1):
                    self.ljono[j]=self.ljono[j + 1]
                self.alkioiden_lkm -=1
                return True
        return False

    def kopioi_lista(self, vanha_lista, uusi_lista):
        for i in range(len(vanha_lista)):
            uusi_lista[i] = vanha_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()

        for numero in a.to_int_list():
            x.lisaa(numero)

        for numero in b.to_int_list():
            x.lisaa(numero)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        b_taulu = b.to_int_list()

        for numero in a.to_int_list():
            if numero in b_taulut:
                    y.lisaa(numero)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        b_taulu = set(b.to_int_list())

        for numero in a.to_int_list():
            if numero not in b_taulut:
                z.lisaa(numero)

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm]))+ "}"