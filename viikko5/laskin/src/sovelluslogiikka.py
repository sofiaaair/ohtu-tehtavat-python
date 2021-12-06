class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.arvo = 0

    def miinus(self, arvo):
        self.arvo = arvo
        self.tulos = self.tulos - self.arvo

    def plus(self, arvo):
        self.arvo = arvo
        self.tulos = self.tulos + self.arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.arvo = arvo
        self.tulos = self.arvo
