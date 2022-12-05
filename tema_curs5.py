# 1.
# def afla_suma():
#     x = 6
#     y = 7
#     suma = x + y
#     return suma
# print(f'Suma celor doua numere este {afla_suma()}')
# afla_suma()

# def afla_suma(x, y):
#     suma = x + y
#     return suma
# print(f'Suma celor doua numere este {afla_suma(5, 10)}')
# print(f'Suma celor doua numere este {afla_suma(12, 14)}')

# 2.
# def adevarat_fals(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# print(adevarat_fals(4))
# print(adevarat_fals(5))

#3.
# def nr_caractere():
#     nume = 'Hassanein'
#     prenume = 'Simona'
#     nume_prenume = len(nume) + len(prenume)
#     return nume_prenume
#
# print(f'Numarul total de caractere al numelui meu este {nr_caractere()}')
# print(f'Numarul total de caractere al numelui meu este {nr_caractere()}')

# 4.
# def aria_dreptunghiului(L, l):
#     aria = L * l
#
#     return aria
# print(f'Aria dreptungiului este de {aria_dreptunghiului(10, 7)} cm patrati.')
# print(f'Aria dreptungiului este de {aria_dreptunghiului(8, 3)} cm patrati.')

# 5.
# def aria_cercului(r):
#     pi = 3.14
#     aria = 3.14 * r ** 2
#
#     return aria
# print(f'Aria cercului este de {aria_cercului(2)} cm patrati.')
# print(f'Aria cercului este de {aria_cercului(1)} cm patrati.')

# 6.
# def caracter(x):
#     string = 'Ciresica vinde mere.'
#     if x in string:
#         return True
#     else:
#         return False
#
# print(caracter('v'))
# print(caracter('u'))
# print(caracter('r'))
# print(caracter('V'))
# print(caracter('b'))


# 7.
# def nr_caractere(str):
#     numara = 0
#     for caracter in str:
#         if caracter.isupper():
#             numara += 1
#         else:
#
#     return numara
# numara = nr_caractere('Fat Frumos si Ileana Cosanzeana')
# print(numara)

# def nr_lower_and_upper(string):
#     lower = 0
#     upper = 0
#     for i in string:
#         if (i.islower()):
#             lower += 1
#         else:
#             upper += 1
#     print(f'Nr de caractere lower case este {lower}')
#     print(f'Nr de caractere upper case este {upper}')
# nr_lower_and_upper('FatFrumos')
# nr_lower_and_upper('IleanaCosanzeana')
# nr_lower_and_upper('JeSSy')

# 8.
# def arata_numere_pozitive(*nr):
#     lista1 = [*nr]
#     lista2 = []
#     i = 0
#     for i in lista1:
#         if i > 0:
#             lista2.append(i)
#             i += 1
#
#     return lista2
# print(f'Numerele pozitive din lista 1 sunt {arata_numere_pozitive(-2, 8, -9, 3, 2, -6)}.')
# print(f'Numerele pozitive din lista 1 sunt {arata_numere_pozitive(3, 5, -7, -2, 9, 10, 205)}.')

# 9.
# def comparatie_de_numere(x, y):
#     if x > y:
#         print(f'Primul număr, {x} este mai mare decat al doilea nr {y}.')
#     elif x < y:
#         print(f'Al doilea nr, {y} este mai mare decat primul nr {x}.')
#     else:
#         print(f'Numerele sunt egale.')
# comparatie_de_numere(2, 5)
# comparatie_de_numere(9, 2)
# comparatie_de_numere(100, 100)
# comparatie_de_numere(150, 134)
# comparatie_de_numere(2345, 4567)
# comparatie_de_numere(90, 90)

# 10.
# incercari:
# def numar_in_set(a, setul):
#
#     if a in setul:
#
#         print(f'Nu am adaugat numărul în set. Acesta există deja.')
#         return False
#         # setul.add(a)
#         # print(f'Am adaugat numărul nou în set.')
#         # return True
#     else:
#         setul.add(a)
#         print(f'Am adaugat numărul nou în set.')
#         return True
#         # setul.discard(a)
#         # print(f'Nu am adaugat numărul în set. Acesta există deja.')
#         # return False
# setul = set()
# # numar_in_set(0, {1, 2, 4})
# print(numar_in_set(0, {1, 2, 4}))
# print(numar_in_set(4, {0, 2, 3, 4}))

# def numar_in_set(a, setul):
#     a = 0
#     for a in setul:
#         print(f'Nu am adaugat numărul în set. Acesta există deja.')
#         return False
#         # setul.add(a)
#         # print(f'Am adaugat numărul nou în set.')
#         # return True
#     else:
#         # setul.add(a)
#         print(f'Am adaugat numărul nou în set.')
#         return True
#         # setul.discard(a)
#         # print(f'Nu am adaugat numărul în set. Acesta există deja.')
#         # return False
# setul = set()
# # numar_in_set(0, {1, 2, 4})
#
# print(numar_in_set(5, {1, 2, 4}))
# print(numar_in_set(2, {0, 2, 3, 4}))

# varianta buna:
# def numar_in_set(a, setul):
#     if a in setul:
#         print(f'Nu am adaugat numărul în set. Acesta există deja.')
#         return False
#     else:
#         setul.add(a)
#         print(f'Am adaugat numărul nou în set.')
#         return True
# setul = set()
# print(numar_in_set(0, {1, 2, 4}))
# print(numar_in_set(4, {0, 2, 3, 4}))
# print(numar_in_set(6, {4, 12, 30, 42}))
# print(numar_in_set(15, {10, 21, 33, 40, 15}))

# Optionale:
# 1.
# from calendar import monthrange
# def numar_de_zile_in_luna(an, luna):
#     return monthrange(an, luna) [1]
# print(numar_de_zile_in_luna(2022, 2))
# print(numar_de_zile_in_luna(2022, 7))
# print(numar_de_zile_in_luna(2022, 4))
# print(numar_de_zile_in_luna(2024, 2))

# def numar_dr_zile_in_luna(luna):
#     if luna == 'ianuarie' and 'martie' and 'mai' and 'iulie' and 'august' and 'octombrie' and 'decembrie':
#         print(31)
#     elif luna == 'februarie':
#         print(28)
#     elif luna == 'aprilie' and 'iunie' and 'septembrie' and 'noiembrie':
#         print(30)
#     else:
#         print('Nu exista aceasta luna.')
#         # print(30)
#
# numar_dr_zile_in_luna('februarie')
# numar_dr_zile_in_luna('ianuarie')
# numar_dr_zile_in_luna('iunie')
# numar_dr_zile_in_luna('asff')
# numar_dr_zile_in_luna('septembrie')
# numar_dr_zile_in_luna('mai')
# numar_dr_zile_in_luna('aprilie')
#
# import from calendar monthrange
# def nr_zile_in_luna(month)
#     return

# 2. Functie calculator:
# def calculator(x, y):
#     a = x + y
#     b = x - y
#     c = x * y
#     d = x / y
#     return a, b, c, d
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
# a, b, c, d = calculator(3, 6)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# 3.
# def de_cate_ori_apare_cifra(lista):
#     return {0 : lista.count(0),
#             1: lista.count(1),
#             2: lista.count(2),
#             3: lista.count(3),
#             4: lista.count(4),
#             5: lista.count(5),
#             6: lista.count(6),
#             7: lista.count(7),
#             8: lista.count(8),
#             9: lista.count(9)
#             }
# lista = []
# print(de_cate_ori_apare_cifra([1, 5, 7, 2, 8, 9]))
# print(de_cate_ori_apare_cifra([0, 3, 2, 6, 4, 3, 0, 7, 8, 4, 3]))

# 4.
# def valoarea_maxima(a, b, c):
#     return max(a, b, c)
# print(valoarea_maxima(2, 4, 6))
# print(valoarea_maxima(9, 3, 6))
# print(valoarea_maxima(10, 8, 4))

# 5.
# def suma_tuturor_numerelor(x):
#     i = 0
#     suma = 0
#     while i <= x:
#         suma = suma + i
#         i += 1
#     return suma
# print(suma_tuturor_numerelor(3))
# print(suma_tuturor_numerelor(5))

# Bonus
# 1.
# def numere_dublate(lista1, lista2):
#     nr_comune = {i for i in lista1 if i in lista2}
#     return nr_comune
# print(numere_dublate([1, 4, 6, 8], [1, 3, 5, 8]))
# print(numere_dublate([2, 4, 7, 5], [2, 7, 9, 10]))

# 4.
# from datetime import date as data_n
# def numar_de_zile(data_1, data_2):
#     return (data_2 - data_1).days
#
# data_1 = data_n(2022, 11, 15)
# data_2 = data_n(2023, 5, 6)
# print(f'Pana la ziua mea mai sunt {numar_de_zile(data_1, data_2)} zile.')
#
# data_1 = data_n(2022, 11, 15)
# data_2 = data_n(2022, 12, 25)
# print(f'Pana la Craciun mai sunt {numar_de_zile(data_1, data_2)} zile.')

from datetime import date as data_n
# def numar_de_zile(data_1, data_2):
#     return (data_2 - data_1).days
#
# print(f'Pana la ziua mea mai sunt {numar_de_zile(2022:11:15, 2023:05:06)} zile')

# 3.
# from datetime import datetime
# import time
# def ora_locala(tara):
#     UTC = datetime
#     return UTC
# print(ora_locala('Romania'))
# >>> from datetime import datetime, timedelta
# >>> from pytz import timezone
# >>> import pytz
# >>> utc = pytz.utc
# >>> utc.zone
# 'UTC'
# >>> eastern = timezone('US/Eastern')
# >>> eastern.zone
# 'US/Eastern'
# >>> amsterdam = timezone('Europe/Amsterdam')
# >>> fmt = '%Y-%m-%d %H:%M:%S %Z%z'
# >>> loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
# >>> print(loc_dt.strftime(fmt))
# 2002-10-27 06:00:00 EST-0500
# ams_dt = loc_dt.astimezone(amsterdam)
# ams_dt.strftime(fmt)

# from datetime import datetime, timedelta
# from pytz import timezone
# import pytz
# def dat_si_ora_locala():
#     utc = pytz.utc
#     utc.zone

# from datetime import datetime
# import pytz
#
# def ora_si_data_locala(datetime):
#     UTC = pytz.utc
#     IST = pytz.timezone('Europe/Bucharest')
#     print(f'Ora si data in Romania este:', datetime.now(IST))
#
# ora_si_data_locala(datetime)
# from datetime import datetime
# import pytz
#
# def ora_si_data_locala(datetime):
#     # UTC = pytz.utc
#     IST = pytz.timezone('Europe/Bucharest')
#     print(f'Ora si data in China este:', datetime.now(IST))

# ora_si_data_locala(datetime)

#2.
# def pret_redus(pret, reducere):
#     pret_final = pret - (reducere * pret) / 100
#     if reducere <= 100:
#         return pret_final
#     else:
#         print('Reducerea e invalida.')
#
# print(f'Pretul redus este: {pret_redus(100, 20)} RON.')
# print(f'Pretul redus este: {pret_redus(100, 120)} RON.')
# print(f'Pretul redus este: {pret_redus(100, 100)} RON.')