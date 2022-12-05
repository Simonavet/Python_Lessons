# Pilonii oop - concepte de baza pt usurarea muncii
# mostenirea, polimorfismul, abstractizarea, incapsularea

# Mostenirea
# - ne ajuta sa nu scriem mult cod
# Clasa parinte si clasa copil unde folosim aceleasi atribute si metode
# 3 tipuri - unica
# - pe mai multe niveluri - parinte - copil - copil1
# mostenire multipla - nu e ok sa o utilizam

# Ex. 1

# class Chef(): # clasa parinte
#     cutite = None
#     linguri = None
#     def __init__(self, nr_cutite):
#         self.cutite = nr_cutite
#     def make_salad(self):
#         print('salad')
#     def make_fries(self):
#         print('fries')
#
# class Chef2():
#     sort = 2
#
# class JapaneseChef(Chef): # punem clasa pe care vrem sa o mostenim - clasa copil
#     def __init__(self, cantitate_alge, cutite):  # cutite nu e la fel cu cele de sus
#         self.alge = cantitate_alge
#         self.cutite = cutite
#     def make_sushi(self):
#         print('sushi')
#
# class ItalianChef(Chef, Chef2): # mostenire multipla
#     tava = 1
#     def make_pizza(self):
#         print('pizza')
#
# new_chef = Chef(4)
# new_chef.make_fries()
#
# japan_chef = JapaneseChef(10, 5)
# japan_chef.linguri = 6
# print(japan_chef.linguri)
# japan_chef.make_sushi()
# japan_chef.make_salad()
#
# mario_chef = ItalianChef(3)
# print(mario_chef.tava)
# print(mario_chef.sort)
# print(mario_chef.linguri)
# mario_chef.linguri = 15
# print(mario_chef.linguri)
#
# class Tokyo_Chef(JapaneseChef):
#     alge = 300
#
# san_chef = Tokyo_Chef(150, 7)
# san_chef.make_salad()

# Ex. 2

# class Animale():
#     sunet = None
#     culoare = None
#     specie = None
#     varsta = 0
#     sunet_somn_mancare = None
#     def dormi(self):
#         print(f'Acum dorm {self.sunet_somn_mancare}')
#     def imbatranire(self):
#         self.varsta = self.varsta + 1
#         print(f'Acum am {self.varsta} ani.')
#
# class Pisica(Animale):
#     toarce = 'Da'
#     vaneaza_soareci = None
#     def toarce_sa_ceri_mancare(self):
#         if self.toarce == 'Da':
#             self.sunet_somn_mancare = 'Meow' # sunet_somn_mancare de aici e doar pt clasa pisica, mosteneste don clasa animale doar dupa instantiere
#             print(self.sunet_somn_mancare)
#
# pisica = Animale()
# pisica_mosteniroare = Pisica()
#
# pisica.sunet = 'Miau, miau'
# print(pisica.sunet)
# print(pisica_mosteniroare.sunet) #obiectele mostenitoare primesc atributele nealterate, trebuie denumite de la 0
# pisica.dormi()
# pisica_mosteniroare.dormi()
# pisica.imbatranire()
# pisica_mosteniroare.imbatranire()

# Plimorfism
#creeam 2 functii cu nume identic dar comportament diferit
# cu numar indefinit de argumente

# print(len('abc'))
# print(len([1,2,3,4]))
#
# def suma_numere(*args): # functie polimorfica
#     sum = 0
#     for elem in args:
#         sum = sum+elem
#     return sum
#
# print(suma_numere(2,4))
# print(suma_numere(4, 6, 9))
# print(suma_numere(10, 6, 9, 8))


# functie cu parametri initializati cu valoare default
# def add(x, y=0, z=0):
#     return x+y+z
# print(add(5))
# print(add(9, 10))
# print(add(1,5, 7))


# polimorfism prin implementarea aceleasi metode in 2 clase diferite

# class America:
#     limba = 'engleza'
#     imn = 'inmnul americii'
#     drapel = 'drapel american'
#     def printeaza_limba(self):
#         print(f'limba care se vorbeste in a va fi {self.limba}')
# class Romania:
#     limba = 'romana'
#     imn = 'desteapta-te romane'
#     drapel = 'tricolor'
#     def printeaza_limba(self):
#         print(f'limba care se vorbeste in ro va fi {self.limba}')
#
# america1 = America()
# romania1 = Romania()
#
# america1.printeaza_limba()
# romania1.printeaza_limba()
#implementarea aceleasi metode in 2 clase diferite


#polimorfism prin reimplementarea aceleasi metode din clasa parinte in clasa copil
# class Pasare:
#     def describe(self):
#         print('sunt o pasare')
#     def zboara(self):
#         print('sunt o pasare, deci zbor')
# class Papagal(Pasare):
#     def vorbeste(self):
#         print('sunt o pasare si vorbesc, deci sunt un papagal')
# class Pinguin(Pasare):
#     def zboara(self):
#         print('nu pot zbura, dar sunt imbracat frumos')
#
# pasare_1 = Pasare()
# pasare_1.describe()
# pasare_1.zboara()
# print('*********************************************************')
# papagal1 = Papagal()
# papagal1.describe()
# papagal1.zboara()
# papagal1.vorbeste()
# print('*******************************************')
# pinguin1 = Pinguin()
# pinguin1.describe()
# pinguin1.zboara() # chiar daca mostenim metoda, daca are aceeasi denumire se reimplementeaza cu ce scriem in clasa copil

#abstractizarea si incapsularea - nu prea le intalnim in testare automata - vezi notite de curs
#keyword pt absratctizare - e nevoie de decorator - intrebare la interviu
#ascundem cod prin abstractizare - corpul metodei

# Abstractizarea
from abc import ABC, abstractmethod # avem nevoie de importurile acestea pentru abstractizare in python
from functools import wraps

#
# class Car(ABC): # Am definit clasa Car care mosteneste conceptul de abstractizare (fara mostenirea asta nu o putem face abstracta)
#
#     @abstractmethod # am folosit un decorator ca sa marcam metoda ca abstracta
#     def accelerate(self): # am inceput definirea metodei abstracte = metode fara corp (logica interna)
#         # in general metodele abstracte nu trebuie sa aiba logica, si atunci pentru a nu avea erori avem doua optiuni:
#         pass   # scriem pass
#         # raise NotImplementedError - ridicam o exceptie de NotImplemented
#
#     def stop(self): # O clasa abstracta poate sa contina si metode normale (care au logica interna)
#         print("STOP!")  #  metodele de clasa, cu logica, nu este obligatoriu sa fie implementate in clasele mostenitoare
#                                 # decoratorul classmethod e optional, dar de regula il punem pentru claritate
#
# # Aici am definit o clasa noua numita Ferrari care mosteneste clasa abstracta Car, ceea ce inseamna ca noi vom fi
#                         # fortati sa implementam metoda abstracta accelerate
#
#
# def upper_case(func):
#     @wraps(func)
#     def func_wrapper(text):
#         return func().upper()
#     return func_wrapper
#
# @upper_case
# def accelerate(text):
#     print(text)
#
# # accelerate('text')
#
# class Ferrari(Car):
#     culoare = None
#
#     def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
#         print("test")  # puteti sa incercati sa o comentati sa vedeti ce se intampla
#
#     def stop(self): # poly
#         print("I'm a F, I can't stop")
#
# # Am implementat din nou o clasa care mosteneste clasa abstracta Car. Aici de asemenea suntem obligati sa implementam metoda accelerate
#
# class Lastun(Car):
#     def accelerate(self):
#         print("I'm accelerating from 0 to 100 in 15 seconds")
#
#
# f = Ferrari()
# f.accelerate()
# f.stop()
#
# l = Lastun()
# l.accelerate()
# l.stop()


# Mai jos am definit o Interfata - adica o clasa abstracta in care toate metodele sunt abstracte (An interface is a completely "abstract class")
# Obliga clasele mostenitoare sa implementeze functiile, e ca o reteta pentru subclase

# class Animal(ABC): # ABC  =  Abstract Base Class
#
#     @abstractmethod  # decorator care marcheaza metoda ca fiind abstracta
#     def sound(self):
#         raise NotImplementedError
#
#     #  pass = cuvant cheie care defineste faptul ca corpul metodei nu are o logica efectiva, dar este folosit pentru ca acea metoda
#          # sa poata sa aiba un corp
#     #  raise NotImplementedError = modalitate prin care putem sa fortam in mod explicit exceptia de not implemented
#
#     @abstractmethod
#     def sleep(self):
#         pass
#
#
# # Atunci cand o clasa mosteneste o alta clasa de tip interfata sau clasa abstracta, spunem ca o implementeaza
#
# class Dog(Animal):
#
#     def sound(self):
#         print('Ham Ham!')
#
#     def sleep(self):
#         print('zzzzzzzzz')
#
#     def describe(self):
#         print('I have an owner')
#
#
# class Cat(Animal):
#     def sound(self):
#         print('Miau Miau!')
#
#     def sleep(self):
#         print('prrrrr')
#
#     def describe(self):
#         print('I own a human')
#
# azorel = Dog()
# tom = Cat()
# azorel.sleep()
# azorel.sound()
# azorel.describe()
#
# tom.sleep()
# tom.sound()
# tom.describe()

# Incapsularea
class Car:
    __color = 'gray'
    _variabila_protected = "Test"
    def __init__(self,var_protected):
        self._variabila_protected = var_protected

    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita

    def delete_color(self):
        self.__color = None

    def __hidden(self):
            print(self._variabila_protected)

volvo = Car("test_attribute")
print(volvo.get_color()) # getter
volvo.set_color('red') # setter
print(volvo.get_color()) # getter
volvo.delete_color() # deleter
print(volvo.get_color()) # getter
print(volvo._variabila_protected)

class CarPy(Car):

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        if color == 'black':
            self.__color = 'gray'
        else:
            self.__color = color
        print(f'Setter: Noua culoare este {color}')

    @color.deleter
    def color(self):
        print(f'Deleter: Am sters culoarea')
        self.__color = None

car2 = CarPy('gray')
car2.color
car2.color = 'red' # set color
car2.color # get color
del car2.color # del color
car2.color # get color
print('--------------------------------')
car3 = CarPy('white')
print(car3.color) # get color
car3.color = 'black'
print(car3.color)
del car3.color
print(car3.color)


class Student:
    _schoolName = 'XYZ School'  # atribut protected
    __schoolNamePrivate = "Test"

    def __init__(self, name, age):
        self._name = name
        self.__age = age

std = Student("Swati", 25)
print(std._schoolName) # atributele protected pot sa fie folosite, dar nu apar intre sugestii atunci cand folosim std.
# print(std.__age) Atributele private nu pot sa fie accesate deloc
# print(std.__schoolNamePrivate)
# print(std.__schoolNamePrivate) - Va returna eroare: AttributeError: 'Student' object has no attribute '__schoolNamePrivate'
# _ceva = protected
# __ceva = private