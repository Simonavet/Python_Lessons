# x = int(input('Scrie un numar, te rog: '))
# if x >= 0:
#     print('Este numar natural')
# else:
#     print('Nu este numar natural')

# x = int(input('Scrie un numar, te rog: '))
# if x < 0:
#     print('Este un numar negativ')
# elif x == 0:
#     print('Este un numar neutru')
# else:
#     print('Este un numar pozitiv')

# x = int(input('Scrie un numar, te rog: '))
# y = int(input('Mai scrie un numar, te rog: '))
# if x-y < 5:
#     print('Diferenta este mai mica decat 5')
# else:
#     print('Diferenta nu este mai mica decat 5')

# x = int(input('Scrie un numar, te rog: '))
# if -2 < x < 13:
#     print('Numarul este intre -2 si 13.')
# else:
#     print('Numarul nu este intre -2 si 13.')

# x = int(input('Scrie un numar, te rog: '))
# if not(5<x<27):
#     print('Numarul nu este intre 5 si 27.')
# else:
#     print('Numarul este intre 5 si 27.')

# x = int(input('Scrie un numar, te rog, X = '))
# y = int(input('Mai scrie un numar, te rog Y = '))
# if x==y:
#     print('X este egal cu Y')
# elif x>y:
#     print('X este mai mare decat Y')
# elif y>x:
#     print('Y este mai mare decat X')
# else:
#     print('X este egal cu Y')

# x = int(input('O latura a unui triunghi are dimensiunea de x = '))
# y = int(input('A doua latura a aceluiasi triunghi are dimensiunea de y = '))
# z = int(input('A treia latura a triunghiului are dimensiunea de z = '))
# if x == y == z:
#     print('Triunghiul este echilateral.')
# elif x == y != z:
#     print('Triunghiul este isoscel.')
# elif x == z != y:
#     print('Triunghiul este isoscel.')
# elif y == z != x:
#     print('Triunghiul este isoscel.')
# else:
#     print('Este un triunghi oarecare.')

# litera = input('Verifica daca litera este vocala. Te rog scrie o litera: ')
# if litera in('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
#     print('Este vocala.')
# else:
#     print('Nu este vocala.')

# nota = int(input('Introdu punctajul obtinut aici: '))
# if 9 < nota <= 10:
#     print('Ai obtinut nota A.')
# elif 8 < nota <= 9:
#     print('Ai obtinut nota B.')
# elif 7 < nota <= 8:
#     print('Ai obtinut nota C.')
# elif 6 < nota <= 7:
#     print('Ai obtinut nota D.')
# elif 4 < nota <= 6:
#     print('Ai obtinut nota E.')
# elif nota <= 4:
#     print('Ai obtinut nota F.')
# else:
#     print('Punctajul nu este recunoscut')

# x = int(input('Descopera daca numarul este par sau impar. Introdu numarul: '))
# if x % 2 == 0:
#     print('Este numar par')
# else:
#     print('Este numar impar')

# x = int(input('Scrie un numar, te rog: '))
# if len(str(x)) >= 4:
#     print(f'{x} are minim 4 cifre.')
# else:
#     print(f'{x} nu are minim 4 cifre.')

# x = int(input('Scrie un numar, te rog: '))
# if len(str(x)) == 6:
#     print(f'{x} are 6 cifre.')
# else:
#     print(f'{x} nu are 6 cifre.')

# x = int(input('Scrie un numar, te rog, X = '))
# y = int(input('Mai scrie un numar, te rog Y = '))
# z = int(input('Mai scrie inca un numar, te rog Z = '))
# list1 = [x, y, z]
# print('Cel mai mare numar este: ', max(list1))

# x = int(input('Unghiul < ABC = '))
# y = int(input('Unghiul < BAC = '))
# z = int(input('Unghiul < ACB = '))
# if x + y + z == 180:
#     print('Triunghiul este valid.')
# else:
#     print('Triunghiul nu este valid.')

# string = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Scrie un numar: '))
# print(string[:len(string)-x])

# string = 'Coral is either the stupidest animal or the smartest rock'
# string_nou = string[0:5] + string[-5:]
# print(string_nou)

# string = 'Coral is either the stupidest animal or the smartest rock'
# string2 = string[-4:]
# print(string2[0])
# print(string2)
# def firstLetter(string2):
#     return(string2[0])
# string = 'Coral is either the stupidest animal or the smartest rock'
# string2 = string[-4:]
# print(string2.index('r'))

# string = 'Coral is either the stupidest animal or the smartest rock'
# string2 = string[-4:]
# print(string.removesuffix(string2))
# print(string2)
# string3 = string.split(sep= ' ')
# last = string3.pop()
# string = string3
# print(string)
# print(str(len(string)-len(string2)))
# print(string.split(sep= ' '))

# string3 = string[:-int(string2)]
# print(string3)

# print(string[::].get(string2[::]))
# print(string[:].removesuffix(string2))

# num_string = '0123456789'
# print(num_string[::2])
# num_string = '0123456789'
# print(num_string[1::2])

# cuvant = input('Verifica daca se termina cu acelasi caracter cuvantul: ')
# if cuvant[0] == cuvant[-1:]:
#     print('Se termina cu aceeasi litera')
#     assert cuvant[0] == cuvant[-1:], "Error: Nu se termina cu aceeasi litera"
# elif cuvant[0].upper() == cuvant[-1].upper():
#     print('Se termina cu aceeasi litera')
#     assert cuvant[0].upper() == cuvant[-1].upper(), "Error: Nu se termina cu aceeasi litera"
# else:
#     print('Nu are aceeasi litera la sfarsit')
#     assert cuvant[0] == cuvant[-1:], "Error: Nu se termina cu aceeasi litera"

import random
dice_roll = random.randint(1,6)
numar = int(input('Ghiceste un numar: '))
print(dice_roll)
if dice_roll>numar:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar} dar a fost {dice_roll}')
elif dice_roll<numar:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {numar} si zarul a fost {dice_roll}')
