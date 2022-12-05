from abc import ABC, abstractmethod
class FormaGeometrica(ABC):

     @abstractmethod
     def aria(self):
         PI = 3.14
         pass
     def descrie(self):
         print('Cel mai probabil am colturi.')

class Patrat(FormaGeometrica):
    __latura = 0
    def __init__(self, latura):
        self.__latura = latura
    def get_latura(self):
        return self.__latura
    def set_latura(self, latura_noua):
        self.__latura = latura_noua
    def delete_latura(self):
        self.__latura = 0
    def aria(self):
        suprafata = self.__latura**2
        print(f'Aria este de {suprafata} cm patrati.')

class Cerc(FormaGeometrica):
    __raza = 0
    def __init__(self, raza):
        self.__raza = raza
    def get_raza(self):
        return self.__raza
    def set_raza(self, raza_noua):
        self.__raza = raza_noua
    def delete_raza(self):
        self.__raza = 0
    def aria(self):
        PI = 3.14
        suprafata = PI * self.__raza**2
        print(f'Aria este de {suprafata} cm patrati.')
    def descrie(self):
        print('Eu nu am colturi')

patrat = Patrat(5)
print(patrat.get_latura())
patrat.set_latura(4)
print(patrat.get_latura())
patrat.aria()
print(patrat.delete_latura())
patrat.descrie()

cerc = Cerc(2)
print(cerc.get_raza())
cerc.set_raza(3)
print(cerc.get_raza())
cerc.aria()
cerc.descrie()
print(cerc.delete_raza())