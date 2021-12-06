class Summa:

    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
    def suorita(self):
       self.sovelluslogiikka.plus(self.syote)
