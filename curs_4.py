#tuple = pe baza de index, sunt imutabile, nu se modifica valoarea, nu se pot sterge elemente
# definire tuplu gol
# t = ()
# print(type(t))
# definire tuplu populat
# t = ('mere', 'pere', 'nectarine', 'gutui', 'pere')
# print(t)
#functii:
# l = []
#index
# print(t.index('nectarine'))
# #count
# print(t.count('pere'))
#remove - da eroare, nu se poate folosi la tuplu
# t.remove('gutui')
# print(t)

#dictionare - sunt ordonate, au specificul cheie - valoare, cheile trebuie sa fie unice
# cheile servesc drept inlocuitor pt index
# sunt ordonate
# cheia in stanga, valoarea in dreapta, se despart prin virgula

# definire
# dictionar gol
# d = {}
# print(type(d))
# dictionar populat
d = {
    'Marca': 'Audi',
    'Model': 'TT',
    'An_fabricatie': 2010,
    'Norma_euro': 'Euro 4',
    'Combustibil': 'Benzina',
    'Model': 'TT'
}
# print(d)
# # functii
# # accesarea elementelor
# print(f'Numele masinii este {d["Marca"]}')
# print(f'Numele masinii este', d.get('Model'))
#
# # adaugare de elemente
# d['Numar_de_locuri'] = 5
# print(d)

#update - actualizam elemente
# d.update({'Numar_de_locuri': 5})
# print(d)
# updates = {'numar_de_locuri': 5}
# print(d)
# ramona = {'Centuri': True}
# d.update(ramona)
# print(d)

#stergerea unui element
# d.pop('Norma_euro')
# print(d)

#accesam cheie prin valori
print(f'Valorile proprietatilor masinii mele sunt {d.values()}')
print(f'Proprietatile masinii mele sunt', d.keys())

#accesare perechi cheie-valoare
print(f'Dictionarul este format din urmatoarele elemente {d.items()}')

#dictionar imbricat - dictionar in dictionar
# apa_plata = {
#     "borsec": {
#         "nume": "borsec",
#         "producator": "borsec",
#         "cantitate_vanzare": "500ml",
#         "impachetare": "baxuri"
#     },
#     "aqua carpatica": {
#         "nume": "aqua carpatica",
#         "cantitate_vanzare": "2l",
#         "impachetare": "sticla"
#     },
#     "dorna":
#         {
#             "nume": "dorna",
#             "producator": "dorna",
#             "impachetare": "bax",
#             "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lumea"},
#             "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
#         }
# }
# # print(apa_plata)
# print(apa_plata['aqua carpatica']['impachetare'])
# print(apa_plata['dorna']['promovare']['reclama'])

# Structuri repetitive
#1. while - executam o serie de instructiuni atat timp cat o conditie este adevarata
# elementul sau variabila de control se declara inafara while-lului
#ex. 1 printati toate nr de la 1 la 10
# i = 1
# while i <= 10:
#     print(f'numarul curent este {i}')
#     i = i + 1

#ex. 2 printam 101 dalmatieni
# dalmatianul = 1
# while dalmatianul <= 101:
#     print(f'Dalmatianul curent are numarul {dalmatianul}')
#     dalmatianul = dalmatianul + 1

# ex. 3 printati suma numerelor de la 1 la 10
# i = 0
# suma = 0
# while i <= 10:
#     suma = suma + i
#     i = i + 1
# print(suma)

# ex. 4 parcurgeti o lista si printati fiecare element
l1 = ['ramona', 'dan', 'alex', 'iulia', 'carmen', 'raul', 'ramona2', 'simona', 'silviu']
i = 0
while i < len(l1):
    print(l1[i])
    i = i + 1
print(len(l1))

# ex. 5 inlocuiti-l pe silviu cu andreea
# i = 0
# while i < len(l1):
#     if l1[i] == 'silviu':
#         l1[i] = 'andreea'
#     i = i + 1
# print(l1)

#break
# ex. 6 inlocuiti alex cu adela
# i = 0
# while i < len(l1):
#     if l1[i] == 'alex':
#         l1[i] = 'adela'
#         break
#     i = i + 1
# print(l1)

#2. For - cand vrem sa parcurgem o lista cu scopul de a printa sau modifica elementele
# cand vrem sa executam un set de instructiuni de un numar specific de ori
# structura
# ex. 1 parcurgeti numerele de la 0 la 10 si printati-le pe cele pare
# for i in range(0,11): # capatul superior nu este luat in considerare
#                       # start range are val default 0 si poate fi omisa
#     if i % 2 == 0:
#         print(i)
#     else:
#         print('nu este par')

# for i in range(11): # capatul superior nu este luat in considerare
#                       # start range are val default 0 si poate fi omisa
#     if i % 2 != 0:
#         print(i)
#     else:
#         print('nu este impar')

for i in range(11):
    print(i)
    if i == 5:
        break
