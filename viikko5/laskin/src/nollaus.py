class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
#        self.syote = syote


    def suorita(self):
        return self.sovelluslogiikka.nollaa()
