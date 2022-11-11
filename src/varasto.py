class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):

        self.tilavuus=max(0.0, tilavuus)
        self.saldo=max(0.0, alku_saldo)
        self.saldo=min(self.tilavuus, self.saldo)

    # huom: ominaisuus voidaan myös laskea. 
    # Ei tarvita erillistä kentää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
