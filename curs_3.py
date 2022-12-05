
# structura alternativa if
# if fara identare
a = 5
b = 10
# if a>b:
# print('A este mai mare decat b') # if fara identare nu merge
# #if cu else
# if a>b:
#     print('A este mai mare decat b')
# else:
#     print('Nu este mai mare')

# if cu else
# if a < b:
#     print('b este mai mare decat a')
# elif a==b:
#     print('a egal cu b')
# else:
#     print('Nu este mai mare')
#
# # if cu operatori
# if a < b or a == b:
#     print('mesaj 1')
# else:
#     print('mesaj2')
'''
Exercitiul 4
RO: Daca un client are peste 65 de ani, atunci va beneficia de o reducere de 15%.
Altfel, daca clientul nu are varsta de peste 65 de ani si calatoreste cu cel putin un copil,
atunci acesta va beneficia de o reducere de 10%.
Pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) se va aplica
o reducere de 10% daca acestia calatoresc iarna.
De asemenea, pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (v
'''
# varsta = int(input('Va rugam introduceti varsta: '))
# anotimp = input('Va rugam sa introduceti anotimpul in care calatoriti: ')
# clasa = int(input("Introduceti clasa: "))
# pretBilet = int(input('Introduceti pretul biletului: '))
# if varsta > 65:
#     discount = 0.15
# else:
#     nrCopii = int(input('Introduceti numarul de copii care va insotesc: '))
#     if nrCopii>=1:
#         discount = 0.1
# if anotimp == 'iarna':
#     discount += 0.1
# if clasa == 1:
#     taxa = 0.03
# else:
#     taxa = 0.01
# pretBilet = pretBilet - pretBilet * discount + pretBilet * taxa
# print((discount, taxa, pretBilet))
# statement covrage - 2 scenarii - verificam cum curge codul ca sa acoperim cel putin o data fiecare instructiune 100%
# decizion covrage - 3 teste - verificam cum curge codul in functie de valorile introduse de la tastatura
# test case = descriere pas cu pas atunci cand verificam o funtionalitate
# avem nevoie de un summary = test condition

# Scenariu: Pers >65 calatoreste iarna la cl 1
# summary = vf faptul ca pt un calator ca si mai sus avem discount de 25% si taxa de 3%
# steps to reproduce:
# 1. intra in aplicatie
# 2. alegem destinatia dorita pt pretul biletului
# 3. completeaza info legate de varsta, sezon si clasa
# 4. verifica pretul calculat al biletului
# Espected result: seniorul va primi o reducere de 25% si va plati o taxa de 3% din pretul biletului, cat plateste deja

#Tipuri de date complexe - structuri de date
# 1. Lista = colectie de date ordonate, tipuri de date diferite sau de acelasi fel
# se scrie intre [] - se defineste cu []
# proprietatea de a fi mutabila
# actiuni asupra unei liste
# - adaugam elemente
# - sterg elemente
# - modificam elemente de la un anumit index
# - sa mutam un element la un anumit index
# 1. declararea si initializarea unei liste goale
a=[]
#2. declararea si initializarea unei liste populate
a_prezenti = ['Raul', 'Simona', 'Alex', 'Dan', 'Ramona1']
a_absenti = ['Silviu', 'Carmen', 'Iulia', 'Ramona']
# string_a = 'Ana are mere si este fericita'
# a_split = string_a.split()
# print(a_split)
# # accesam elemente
# print(f'primul element din lista este: {a_prezenti[0]}')
# print(f'primul element din lista este: {a_absenti[0]}')
# # accesam ultimul element din lista
# print(f'Ultimul element: {a_prezenti[len(a_prezenti)-1]}')
# print(f'Ultimul element: {a_prezenti[-1]}')
# # functia append - adauga la sfarsit
# a_prezenti.append('Adela')
# print(a_prezenti)
# #functia insert - adauga un elemet unde vrem noi
# a_absenti.insert(2, 'Adela')
# print(a_absenti)
# #functia index
# print(a_absenti.index('Iulia'))
# #functia remove - stergem un element pe baza numelui
# print(a_prezenti.remove('Dan')) # nu returneaza nimic
# print(a_prezenti)
# functia pop
print(a_absenti.pop(-1))
print(a_absenti)
#functia count - de cate ori apare un element dintr-o lista
print(a_prezenti.count('Simona'))
# extend
print(a_prezenti.extend(a_absenti)) # nu returneaza nimic
print(a_prezenti)
# clear - sterge continutul listei => lista goala
# sort - sorteaza in ordine alfabetica in functie de codul ascii
## ASCII: https://infoas.ro/lectie/90/codul-ascii-tabel-complet
# a_prezenti.sort()

#liste neomogene - tipuri de date diferite
lista_neomogena = ['maria', 12, True, 15.3]

#2. Seturi
#structuri/colectii de date neordonate, imutabile (nu putem modifica valorile lor), nu accepta duplicate
# definirea: cu o pereche de {}
# operatii: accesare de elemente, adauga elemente, sterge elemente

# definirea unui set gol
# set_gol = set()
# print(type(set_gol))
# definirea unui set populat
set_populat = {'Caine', 'Pisica', 'Hamster', 'Papagal'}
#accesam un element
# operatorul In
print('Hamster' in set_populat)
# assert 'Hamster' in set_populat, "Error: Hamster nu este in set_popular"
# assert 'Gaina' in set_populat, "Error: eroare"

# functii: add()
# set_populat.add('Gaina')
# print(set_populat)
set_populat.add('Pisica')
print(set_populat)
#
# # functia pop
# set_populat.pop()
# print(set_populat)
#
# set_populat.pop()
# print(set_populat)

# functia remove - da eroare daca elementul nu exista
# set_populat.remove('Hamster')
# print(set_populat)

# set_populat.remove('Broasca')
# print(set_populat)

#functia discard - executa daca elementul nu exista
# set_populat.discard('Pisica')
# print(set_populat)

set_populat.discard('Broasca')
print(set_populat)

# functia update
set_populat.update() # concatenare - doar modifica setul
# union
set_populat.union() # creeaza un set nou care reprezinta concatenarea celor 2 seturi
# clear
set_populat.clear()# sterge continutul setului
