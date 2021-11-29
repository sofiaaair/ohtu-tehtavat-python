import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

            if tuote_id == 2:
                return 5

            if tuote_id == 3:
                return 1

            if tuote_id == 4:
                return 0

        def varasto_hae_tuote(tuote_id):
            self.tuoteid = tuote_id
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

            if tuote_id == 2:
                return Tuote(2, "banaani", 3)

            if tuote_id == 3:
                return Tuote(3, "rucola", 2)

            if tuote_id == 4:
                return Tuote(4, "appelsiini", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()


    def test_yhden_tuotteen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345",ANY, 5)


    def test_kahden_eri_tuotteen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_kahden_saman_tuotteen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 6)

    def test_lisataan_loytyva_ja_loppunut_tuote_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(4)
        self.kauppa.tilimaksu("pekka", "2468")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "2468", ANY, 5)


    def test_aloitushetkella_ostoskori_on_tyhja(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "1234")
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("maija", "1256")
        self.pankki_mock.tilisiirto_assert_called_with("maija", ANY, "1256", ANY, 5)


    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.return_value = [55, 62, 33]
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("matti", "1996")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("anu", "3456")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_kauppa_tuotteen_poiston_jalkeen_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.poista_korista(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("matti", "5678")
        self.pankki_mock.tilisiirto.assert_called_with("matti", ANY, "5678", ANY, 3)
