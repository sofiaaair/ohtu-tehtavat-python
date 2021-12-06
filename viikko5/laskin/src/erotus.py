class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote


    def suorita(self):
        return self.sovelluslogiikka.miinus(self.syote)
