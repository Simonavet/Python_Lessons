# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# note_muzicale[::-1]
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)
#
# print(note_muzicale.count('do'))

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista1.extend(lista2)
# print(lista1)

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# print(lista3)
# lista3.sort()
# print(lista3)
#
# lista3.remove(0)
# print(lista3)
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# if lista3 == []:
#     print('Lista este goala.')
# else:
#     print('Lista nu este goala.')

# lista3.clear()
# if lista3 == []:
#     print('Lista este goala.')
# else:
#     print('Lista nu este goala.')

# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())
# print(f'Ana a luat nota' , dict1['Ana'])
# print(f'Gigel a luat nota' , dict1.get('Gigel'))
# print(f'Dorel a luat nota' , dict1['Dorel'])
# dict1['Dorel'] = 6
# print(dict1)
# dict1.pop('Gigel')
# dict1['Ionica'] = 9
# print(dict1)

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# if weekend.issubset(zile_sapt) == True:
#     print('Weekend este un subset al zilelor săptămânii.')
# else:
#     print('Weekend nu este un subset al zilelor săptămânii.')

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# print(zile_sapt.difference(weekend))
# print(weekend.difference(zile_sapt))

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# print(zile_sapt.intersection(weekend))
# print(weekend.intersection(zile_sapt))

echipa = ['Pop', 'Cucu', 'Matis', 'Ion', 'Ispas']
jucator_scos = input('Numeste jucatorul care trebuie sa iasa: ')
jucator_intrat = input('Numeste jucatorul care trebuie sa intre: ')
schimbari_efectuate = int(input('Scrie numarul schimbarii: '))
schimbari_maxime = 3
# if jucator_scos in echipa and schimbari_efectuate <= schimbari_maxime:
#     echipa.remove(jucator_scos)
#     echipa.append(jucator_intrat)
#     print(f'A intrat ', jucator_intrat, ' a ieșit ', jucator_scos, ' mai ai', schimbari_maxime - schimbari_efectuate, 'schimbări.')
#     print(f'Echipa ta este formata din:', echipa)
# elif jucator_scos in echipa and schimbari_efectuate > schimbari_maxime:
#     print('Nu se mai pot face modificari. Ai efectuat toate schimbarile.')
# elif jucator_scos is not echipa and schimbari_efectuate > schimbari_maxime:
#     print('Nu se mai pot face modificari. Ai efectuat toate schimbarile.')
# else:
#     print('Nu se poate efectua schimbarea deoarece jucătorul', jucator_scos, 'nu e în teren.')
#     print(f'Mai ai', schimbari_maxime - schimbari_efectuate + 1, 'schimbări')

if jucator_scos in echipa and schimbari_efectuate <= schimbari_maxime:
    echipa.remove(jucator_scos)
    echipa.append(jucator_intrat)
    print(f'A intrat ', jucator_intrat, ' a ieșit ', jucator_scos, ' mai ai', schimbari_maxime - schimbari_efectuate, 'schimbări.')
    print(f'Echipa ta este formata din:', echipa)
elif schimbari_efectuate > schimbari_maxime:
    print('Nu se mai pot face modificari. Ai efectuat toate schimbarile.')
else:
    print('Nu se poate efectua schimbarea deoarece jucătorul', jucator_scos, 'nu e în teren.')
    print(f'Mai ai', schimbari_maxime - schimbari_efectuate + 1, 'schimbări')

