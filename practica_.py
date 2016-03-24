class Coche:
    def __init__(self, gasolina):
         self.gasolina = gasolina
         print "Tenemos", gasolina, "litros"

    def arrancar(self):
        if gasolina > 0:
            print "Arranca"
        else:
            print "no arranca"

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "no se mueve"

