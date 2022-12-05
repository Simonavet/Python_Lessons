#import oop
from curs_6_to_be_imported import Test_case1, Test_case2, Test_case3

# import din python - se cauta dupa modulul built-in apalendu-se functia import()
# import math
# from math import *
# din modulul built in math importa tot
# daca vrem sa importam o functie concreta - pi
# from math import pi
# functii - continuare
# 1. fctie cu numar indefinit de parametrii - cu args

# def calculeaza_pretul(*pret):
#     total = 0
#     for element in pret:
#         total += element
#     return total
# print(calculeaza_pretul(2, 6, 7))
# print(calculeaza_pretul(1,3))
# print(calculeaza_pretul(1,3,6, 4, 7,8,9))
# print(calculeaza_pretul('casa', 'masina')) #- daca dam int tot timpul punem int nu merge cu string

# functii cu kwargs <=> cu **nume_argument
# in special pt a parcurge dictionare si a opera cu ele
# ** se scrie pt fiecare parametru
# ex. 1
apa = {'Borsec': {'nume': 'Borsec', 'producator': 'Borsec', 'imbuteliere': 'sticla'},
       'Dorna': {'nume': 'Dorna', 'producator': 'Dorna', 'imbuteliere': 'peturi'}
}
def accesarea_elemente_dictionar(**kwargs):
    for key, values in kwargs.items():
        print(f'Detalii despre apa: {key}')
        for key_int, values_int in values.items():
            print(f'Apa {key} are {key_int}: {kwargs[key][key_int]}')
# accesarea_elemente_dictionar(**apa)
# accesarea_elemente_dictionar(apa) - nu merge fara **

def accesarea_elemente_dictionar1(**param1):
    for i, j in param1.items():
        print(f'Detalii despre apa: {i}')
        for key, value in j.items():
            print(f'Apa {i} are {key}: {param1[i][key]}')
accesarea_elemente_dictionar1(**apa)

# OOP = POO = programare orientata pe obiect
# modalitate prin care creem un template pt atributele si comportamentul unui anumit element
# clasa = elementul de baza - tiparul poo
# folosim clasa prin obiect
# obiect = reprezentarea efectiva a unu obiect
# cand creem un obiect = instantiere
# un obiect este o instanta a unei clase
# trecem de la o cl la un ob prin instatiere
# atribute - variabile cu val - proprietatile
# metode = functii - ce actiuni putem face
# ex.
"""Exemplu: Clasa masina (templateul)
Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca
A. O masina de exemplu poate sa aiba urmatoarele PROPRIETATI (<=> ATRTIBUTE):
 - culoare
 - viteza
 - an_fabricatie
 - marca
 - model
 - capacitate_rezervor
 - tip_combustibil
 - tractiune
 - serie_sasiu
 - cutie_viteze
 - numar_inmatriculare
B. O masina poate sa faca urmatoarele ACTIUNI ( <=> METODE)
 - pornire de pe loc
 - oprire
 - accelerare
 - franare
 - consum_instant 
 - re
"""
# definirea unei clase se face ci keywordul - class
# avem nevoie de nume - incepe cu litera mare si in snake_case sau camelCase
# dupa nume - intotdeauna ":"
# class Masina:
    # aici se va scrie corpul
# constructor = agent responsabil cu creearea obiectului
# Vom vb despre 2 tipuri de constructori: impliciti si expliciti
# 1.Construtorul explicit - cel care se defineste de catre programator in cod
# 2.Constructorul implicit - se apeleaza automat de python cand constructorul explicit lipseste/ nu e definit
#                          - este o bucata de cod care se apeleaza de catre Python
# Definirea constructorului: __init__()
# intre paranteze se vor specifica atributele care vrem sa existe in mod obligatoriu la creearea obiectului
# exista situatii in care nu avem nimic intre paranteze. daca nu avem nimic scris(niciun parametru)
# atunci toate atributele vor fi optionale

# Elementul 'self' - un keyword
# ne ajuta sa accesam elemente definite in interiorul clasei - atribute sau metode
# toate trebuie accesate cu self.nume_atribut sau self.nume_metoda

#exemplu: cu constructor implicit
class Scoala:
    # Atribute:
    nume_director = None # string fara valoare - keyword
    nr_clase = 0
    nr_elevi_clasa = 0

    # Metode
    def calc_nr_total_elevi(self, nr_clase, nr_elevi_clasa):
        nr_total_elevi = nr_clase * nr_elevi_clasa
        return nr_total_elevi
# # Instantiem un obiect al clasei scoala care va primi implicit atributele si metodele clasei 'Scoala'
# scoala_Bob = Scoala()
# scoala_Bob.nume_director = 'Ion Bob'
# print(scoala_Bob.nume_director)
# nr_clase = int(input('Introduceti numarul de clase pentru scoala Bob: '))
# nr_elevi_clasa = int(input('Introduceti nr-ul de elevi pt scoala Bob: '))
# print(f'Nr total de elevi din scoala Bob este {scoala_Bob.calc_nr_total_elevi(nr_clase, nr_elevi_clasa)}')
#
# #Am instattiat un nou obiect
# scoala_Popovici = Scoala()
# scoala_Popovici.nume_director = 'Andrei Popovici'
# print(f'Nr total de elevi din scoala Popovici este {scoala_Popovici.calc_nr_total_elevi(25, 15)}') # dam valori

# continut = math.pi
# print(f'Pi are valoarea {continut}')
#
# continut2 = math.factorial(3)
# print(f'Factorial de 3 este {continut2}')

#instantiem
my_test_case1 = Test_case1()
my_test_case2 = Test_case2()
my_test_case3 = Test_case3('Test_case_nr_003', 'The test case validates the design and functionality of the OK button.')

# apelul metodei din test_case1
my_test_case1.printeaza_test_case()
my_test_case2.printeaza_test_case()
my_test_case3.printeaza_test_case()
print(my_test_case3.return_name())
print(my_test_case3.return_summary())

#print(my_test_case1.return_summary()) #nu putem cere metode din alte clase