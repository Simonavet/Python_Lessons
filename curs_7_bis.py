class Masina:
    #definirea atributelor
    model = None
    culoare = 'Orange'
    marca = None
    viteza_maxima = 0
    an_fabricatie = 0
    capacitate_motor = 0
    serie_sasiu = None
    tip_combustibil = 'motorina'
    cutie_viteze = 'automat'
    # viteza_curenta = 0

    #contructor
    def __init__(self, marca1, model1, culoare1):
        self.marca = marca1
        self.model = model1
        if culoare1 == 'Orange':
            self.culoare = 'portocaliu'
        # self.culoare = culoare

    # metode
    def paint(self, colour):
        self.culoare = colour
    def start_masina(self, viteza_curenta):
        viteza_curenta = viteza_curenta + 5
        print('Masina s-a pus in miscare')
        return viteza_curenta

# bmw = obiectul
bmw = Masina('BMW', '1200', 'negru')
bmw.culoare = 'galben'
print(bmw.culoare)
print(bmw.marca)
bmw.paint('verde')
print(bmw.culoare)
print(bmw.start_masina(10))
# cum accesam un atribut in interiorul unei clase? - intrebare examen final = prin keyword "self" self.atribut
#cum pot accesa atributele si metodele unei clase din afara clasei? - intrebare examen final = prin intermediul obiectului

# Pilonii OOP
# 4 piloni - concepte de baza - mostenirea, polimorfismul, incapsularea si abstractizarea

