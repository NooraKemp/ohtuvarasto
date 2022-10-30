import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.negatiivinenVarasto = Varasto(-10, -10)
        self.taysiVarasto = Varasto (10, 11)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.negatiivinenVarasto.saldo, 0)
        self.assertAlmostEqual(self.taysiVarasto.saldo, 10)
        
        tulostus = str(self.varasto)
        self.assertAlmostEqual(tulostus, "saldo = 0, vielä tilaa 10") 

    def test_uuttavarastoa_ei_voi_luoda_negatiivisella_tilavuudella(self):
        self.assertAlmostEqual(self.negatiivinenVarasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivisen_arvon_lisaaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)
 
        # pitäisi olla 0 
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_varastoon_ei_voi_lisata_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)
        
        # varastoon pitäisi pystyä lisäämään vain tilavuus eli saldon pitäisi olla 10
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_maaran_ottaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-1)

        # pitäisi olla 8
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastosta_ei_voi_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(10)

        # ei saa olla negatiivinen arvo, pitäisi olla 0
        self.assertAlmostEqual(self.varasto.saldo, 8)