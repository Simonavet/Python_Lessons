# 1. oop cerc
import math
from math import pi

class Cerc:
    culoare = None
    raza = 0

    def __init__(self, culoare, raza):
        self.culoare = culoare
        self.raza = raza
    def descrie_cerc(self):
        print(f'Cercul este de culoare {self.culoare} si raza de {self.raza} cm.')
    def aria(self):
        aria = pi * self.raza ** 2
        return aria
    def diametru(self):
        print(f'Diametru cercului este de {2 * self.raza} cm.')
    def circumferinta(self):
        print(f'Circumferinta cercului este de {2 * pi * self.raza} cm.')


cercul1 = Cerc('roz', 2)
cercul2 = Cerc('albastra', 3)

cercul1.descrie_cerc()
print(f'Aria cercului este de', cercul1.aria(), 'cm.')
cercul1.diametru()
cercul1.circumferinta()

cercul2.descrie_cerc()
print(f'Aria cercului este de', cercul2.aria(), 'cm.')
cercul2.diametru()
cercul2.circumferinta()


# 2 oop Dreptunghi
# class Dreptunghi():
#     culoare = None
#     L = 0
#     l = 0
#     def __init__(self, culoare):
#         self.culoare = culoare
#     def descrie(self, culoare, L, l):
#         print(f'Dreptunghiul are culoarea {culoare}, lungimea de {L} cm si latimea de {l} cm.')
#     def aria(self, L, l):
#         print(f'Aria dreptunghiului este de {L * l} cm.')
#     def perimetrul(self, L, l):
#         print(f'Perimetrul dreptunghiului este de {2*L + 2*l} cm.')
#     def schimba_culoarea(self, noua_culoare):
#         noua_culoare = self.culoare
#
# dreptunghiul1 = Dreptunghi('galben')
# dreptunghiul2 = Dreptunghi('verde')
#
# dreptunghiul1.descrie('galben', 10, 5)
# dreptunghiul1.aria(10, 5)
# dreptunghiul1.perimetrul(10, 5)
# dreptunghiul1.schimba_culoarea('rosu')
# dreptunghiul1.descrie('rosu', 10, 5)
#
# dreptunghiul2.descrie('verde', 8, 3)
# dreptunghiul2.aria(8, 3)
# dreptunghiul2.perimetrul(8, 3)
# dreptunghiul2.schimba_culoarea('mov')
# dreptunghiul2.descrie('mov', 8, 3)

# class Dreptunghi():
#     culoare = None
#     L = 0
#     l = 0
#     def descrie(self):
#         print(f'Dreptunghiul are culoarea {self.culoare}, lungimea de {self.L} cm si latimea de {self.l} cm.')
#     def aria(self):
#         print(f'Aria dreptunghiului este de {self.L * self.l} cm.')
#     def perimetrul(self):
#         print(f'Perimetrul dreptunghiului este de {2*self.L + 2*self.l} cm.')
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#
# dreptunghiul1 = Dreptunghi()
# dreptunghiul1.culoare = 'galben'
# dreptunghiul1.L = 10
# dreptunghiul1.l = 5
#
# dreptunghiul1.descrie()
# dreptunghiul1.aria()
# dreptunghiul1.perimetrul()
# dreptunghiul1.schimba_culoarea('rosu')
# dreptunghiul1.descrie()
#
# dreptunghiul2 = Dreptunghi()
# dreptunghiul2.culoare = 'verde'
# dreptunghiul2.L = 8
# dreptunghiul2.l = 3
# dreptunghiul2.descrie()
# dreptunghiul2.aria()
# dreptunghiul2.perimetrul()
# dreptunghiul2.schimba_culoarea('mov')
# dreptunghiul2.descrie()

# 3. Angajat
# class Angajat():
#     nume = None
#     prenume = None
#     salariu = 0
#     def descrie(self, nume, prenume, salariu):
#         print(f'Angajatul se numeste {nume} {prenume} si are salariul lunar de {salariu} lei.')
#     def nume_complet(self, nume, prenume):
#         print(f'Angajatul {nume}, {prenume}')
#     def salariu_lunar(self, salariu):
#         print(f'Are salariul lunar de {salariu} lei.')
#     def salariu_anual(self, salariu):
#         salariu_anual = salariu * 12
#         print(f'Si salariul anual de {salariu_anual} lei.')
#     def marire_salariu(self, salariu, procent):
#         salariu_nou = salariu + (salariu * procent)/ 100
#         print(f'Angajatul a primit o marire de {procent} % si acum are salariul de {salariu_nou} lei.')
#
# angajat1 = Angajat()
# angajat2 = Angajat()
#
# angajat1.descrie('Pop', 'Adrian', 6000)
# angajat1.nume_complet('Pop', 'Adrain')
# angajat1.salariu_lunar(6000)
# angajat1.salariu_anual(6000)
# angajat1.marire_salariu(6000, 20)
#
# angajat2.descrie('Smith', 'John', 8000)
# angajat2.nume_complet('Smith', 'John')
# angajat2.salariu_lunar(8000)
# angajat2.salariu_anual(8000)
# angajat2.marire_salariu(8000, 10)

# class Angajat():
#     nume = None
#     prenume = None
#     salariu = 0
#     def descrie(self):
#         print(f'Angajatul se numeste {self.nume} {self.prenume} si are salariul lunar de {self.salariu} lei.')
#     def nume_complet(self):
#         print(f'Angajatul {self.nume}, {self.prenume}')
#     def salariu_lunar(self):
#         print(f'Are salariul lunar de {self.salariu} lei.')
#     def salariu_anual(self):
#         salariu_anual = self.salariu * 12
#         print(f'Si salariul anual de {salariu_anual} lei.')
#     def marire_salariu(self, procent):
#         salariu_nou = self.salariu + (self.salariu * procent)/ 100
#         print(f'Angajatul a primit o marire de {procent} % si acum are salariul de {salariu_nou} lei.')
#
# angajat1 = Angajat()
# angajat1.nume = 'Pop'
# angajat1.prenume = 'Adrian'
# angajat1.salariu = 6000
#
# angajat1.descrie()
# angajat1.nume_complet()
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu(20)
#
# angajat2 = Angajat()
# angajat2.nume = 'Smith'
# angajat2.prenume = 'John'
# angajat2.salariu = 8000
#
# angajat2.descrie()
# angajat2.nume_complet()
# angajat2.salariu_lunar()
# angajat2.salariu_anual()
# angajat2.marire_salariu(10)

# 4. Cont

# class Cont():
#     iban = None
#     titular_cont = None
#     sold = 0
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')
#     def debitare_cont(self, suma):
#         sold_nou = self.sold + suma
#         print(f'Acum aveti in cont suma de {sold_nou} lei.')
#         self.sold = sold_nou
#     def creditare_cont(self, suma):
#         noul_sold = self.sold - suma
#         print(f'Acum mai aveti in cont {noul_sold} lei.')
#
# cont1 = Cont('RO10RT000123', 'Abrudan Catalin', 3000)
# cont2 = Cont('RO10RT000456', 'Ionescu Ana', 4000)
#
# cont1.afisare_sold()
# cont1.debitare_cont(200)
# cont1.creditare_cont(400)
#
# cont2.afisare_sold()
# cont2.debitare_cont(350)
# cont2.creditare_cont(600)

# Exercitii optionale
# 1. Factura

# from datetime import date
# from tabulate import tabulate
# #
# class Factura():
#     seria = 'HS'
#     numar = 0
#     nume_produs = None
#     cantitate = 0
#     pret_buc = 0
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#     def genereaza_factura(self):
#         print(f'Factura seria: {self.seria}, numar {self.numar}')
#         azi = date.today()
#         print(f'Data: {azi}')
#         tabel = [['Produs', 'Cantitate', 'Pret_bucata', 'Total'], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc]]
#         print(tabulate(tabel))
# factura1 = Factura(1, 'Foresto', 3, 100)
# factura2 = Factura(2, 'Scalibor', 2, 110)
#
# factura1.genereaza_factura()
# factura1.schimba_nume_produs('SafePet')
# factura1.schimba_cantitatea(4)
# factura1.schimba_pretul(90)
# factura1.genereaza_factura()
#
# factura2.genereaza_factura()
# factura2.schimba_nume_produs('PetPal')
# factura2.schimba_cantitatea(5)
# factura2.schimba_pretul(70)
# factura2.genereaza_factura()

# 2. Masina

# class Masina:
#     marca = 'Dacia'
#     model = None
#     viteza_maxima = 0
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = {'rosu', 'albastru', 'negru'}
#     inmatriculata = False
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#     def descrie(self):
#         print(f'Marca: {self.marca}; Model: {self.model}; Culoare {self.culoare}; Viteza actuala: {self.viteza_actuala} km/h; Viteza maxima: {self.viteza_maxima} km/h; Inmatriculata: {self.inmatriculata}')
#     def inmatriculare(self):
#         self.inmatriculata = True
#         print(f'Inmatriculata: {self.inmatriculata}')
#     def vopseste(self, noua_culoare):
#         culori_disponibile = {'rosu', 'albastru', 'negru'}
#         if noua_culoare in culori_disponibile:
#             culoare = noua_culoare
#             print(f'Noua culoare este: {culoare}')
#         else:
#             print(f'Eroare: culoarea {noua_culoare} nu este disponibila.')
#     def accelereaza(self, viteza):
#         while viteza > 0:
#             print('vrum, vrum!')
#             viteza = viteza + 1
#             if viteza >= self.viteza_maxima:
#                 print(f'Am ajuns la viteza maxima')
#                 break
#         while viteza <= 0:
#             print('Eroare: nu putem porni')
#             break
#     def franeaza(self):
#         print(f'Am franat si ne-am oprit, avem viteza 0.')
#
#
# masina1 = Masina('Logan', 180)
# masina2 = Masina('Spring', 140)
#
# masina1.descrie()
# masina1.inmatriculare()
# masina1.vopseste('rosu')
# masina1.accelereaza(200)
# masina1.franeaza()
#
#
# masina2.descrie()
# masina2.inmatriculare()
# masina2.vopseste('mov')
# masina2.accelereaza(-20)
# masina2.franeaza()

# 3. ToDoList
#
# class TodoList:
#     todo = {}
#     def adauga_task(self, nume, descriere):
#         self.todo[nume] = descriere
#         print(self.todo)
#     def finalizeaza_task(self, nume):
#         self.todo.pop(nume)
#         print(self.todo)
#     def afiseaza_todo_list(self):
#         print(self.todo.keys())
#     def afiseaza_detalii_suplimentare(self, nume_task):
#         if nume_task not in self.todo:
#             raspuns = input('Vreti sa adaugam noul task? ')
#             if raspuns == 'Nu':
#                 print('La revedere!')
#             elif raspuns == 'Da':
#                 detalii_suplimentare = input('Scrie detaliile, te rog: ')
#                 self.todo[nume_task] = detalii_suplimentare
#                 print(self.todo)
#             else:
#                 print('Eroare: greseala de tipar.')

# todo_list1 = TodoList()
# todo_list1.adauga_task('citeste', 'o carte')
# todo_list1.adauga_task('gateste', 'ceva bun')
# todo_list1.adauga_task('pune la spalat', 'haine')
# todo_list1.finalizeaza_task('gateste')
# todo_list1.afiseaza_todo_list()
# todo_list1.afiseaza_detalii_suplimentare('plimb-o pe Jessy')

# todo_list2 = TodoList()
# todo_list2.adauga_task('plateste', 'facturile')
# todo_list2.adauga_task('verifica', 'numerele de telefon')
# todo_list2.adauga_task('trimite raportul', 'clientului')
# todo_list2.finalizeaza_task('verifica')
# todo_list2.afiseaza_todo_list()
# todo_list2.afiseaza_detalii_suplimentare('scrie un e-mail')
