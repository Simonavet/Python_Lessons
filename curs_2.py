# slicing
#luam elemente din string
#trebuie sa zicem pozitia de start si de sf si din cat in cat
#nu se ia ultimul caracter in considerare
poezie = 'Ana are mere si, este vesela pt ca este miercuri'
# Extrage toate caracterele de la inceput pana sfarsit cu specificarea
# Pozitia de stop len(poezie) reprezinta de fapt lungimea stringurului poezie
# print(poezie[0:len(poezie)])
# print(poezie[:])
# print(poezie[::])
# #extragem toate caracterele de la inceput pana la sfarsit
# #extragem caractere in functie de pas
# print(poezie[0:len(poezie):2])
# print(poezie[::2])
# #extragem caracterele de la pozitia 5 pana la pozitia 13 inclusiv
print(poezie[5:14])
# #extragem caracterele ultimele 3 caractere de la final
print(poezie[len(poezie)-3:len(poezie)])
# #sau
# print(poezie[-3:])
# #printam string in ordine inversa
# print(poezie[::-1])
#metoda split - se returneaza o lista de elemente, iar splitul se va face la fiecare cuvantt
print(poezie.split(sep=','))
print(poezie.split(sep= 'L'))
print(poezie.split(sep= ' '))
#metoda replace - inlocuieste elemente
print(poezie.replace('A', 'm'))
print(poezie.replace('Ana', 'Maria'))
#metoda upper
print(poezie.upper())
#combinam metode
print(poezie.upper().replace('A', 'm'))
#metoda index() si metoda find()
print(poezie.index('A'))
print(poezie.index('a'))
print(poezie.find('a'))
#diferenta dintre find si index este faptul ca find returneaza -1 in cazul in crare
#caracterul nu este gasit,
#iar index ne returneaza o eroare
# print(poezie.find('x'))
# print(poezie.index('x'))
#metoda isnumeric(), metoda count(), metoda capitalize()
numeric = '1234'
print(poezie.isnumeric())
print(numeric.isnumeric())
print(poezie.count('a'))
print(poezie.count('A'))
print(poezie.capitalize())
poezie = 'ana are mere si, este vesela pt ca este miercuri'
print(poezie.capitalize())


