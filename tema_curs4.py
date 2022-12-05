# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# for i in range(len(masini)):
#     print(f'Mașina mea preferată este {masini[i]}')

# for masina in masini:
#     print(f'Mașina mea preferată este {masina}')

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini):
#     print(f'Mașina mea preferată este {masini[i]}')
#     i = i + 1

# 2.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(1, 8):
#     masini[i] = masini[i].upper()
# else:
#     print(masini)

# 3.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if i == 3:
#         print('Am găsit mașina dorită de dvs.')
#         break
#     else:
#         print(f'Am găsit mașina {masini[i]}. Mai căutam.')

# 4.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if i == 5:
#         continue
#     elif i == 7:
#         continue
#     print(f'S-ar putea să vă placă mașina {masini[i]}')

# 5.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in range(len(masini)):
#     if i == 5:
#         masini_vechi.append(masini[i])
#         masini.pop(i)
#     elif i == 6:
#         masini_vechi.append(masini[i])
#         masini.pop(i)
# masini.append('Tesla')
# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi: {masini[-1]}')
# print(masini)
# print(masini_vechi)

#6
# pret_masini = {
#                'Dacia': 6800,
#                'Lastun': 500,
#                'Opel': 1100,
#                'Audi': 19000,
#                'BMW': 23000
# }
# for key, value in pret_masini.items():
#     if value <= (15000):
#         print(key, value)

# pret_masini = {
#             'Dacia': 6800,
#             'Lastun': 500,
#             'Opel': 1100,
#             'Audi': 19000,
#             'BMW': 23000
# }
# for key, value in pret_masini.items():
#         if value <= (15000):
#             print(f'Pentru un buget de sub 15000 euro puteti alege mașina', key)

# 7.
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# de_cate_ori = 0
# for i in numere:
#     if i == 3:
#         de_cate_ori += 1
# print(de_cate_ori)

# 8
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# i = 0
# total = 0
# while i < len(numere):
#     total = total + numere[i]
#     i = i + 1
# print(total)
# 9
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# cel_mai_mare_numar = numere[0]
# for nr in numere:
#     if nr > cel_mai_mare_numar:
#         cel_mai_mare_numar = nr
# print(cel_mai_mare_numar)

# 10
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numere2 = []
# for nr in numere:
#     if nr > 0:
#         numere2.append(-abs(nr))
#     else:
#         numere2.append(abs(nr))
# print(numere2)

# ex optionale
# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for nr in alte_numere:
#     if nr % 2 == 0:
#         numere_pare.append(nr)
#     elif nr % 2 != 0:
#         numere_impare.append(nr)
# for nr in alte_numere:
#     if nr > 0:
#         numere_pozitive.append(nr)
#     elif nr < 0:
#         numere_negative.append(nr)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)):
#     for j in range(i + 1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
#
# print(alte_numere)

#Cum aranjam numerele dintr-o lista in ordine crescatoare fara functia sort()
# my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []
#
# while my_list:
#     min = my_list[0]
#     for x in my_list:
#         if x < min:
#             min = x
    # new_list.append(min)
    # my_list.remove(min)

# print(new_list)

# my_list = [4, 2, 3, -1, -2, 0, 1]
#
# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):
#
#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i]
#
# print(my_list)

# 5.
# tastatura_telefon = [
#                  [1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9],
#                  [0]
# ]
# for nr in tastatura_telefon:
#     for j in nr:
#         print(f'Cifra curenta este', j)

# 3.
# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = []
# numar_ales = int(input('Alege un numar:'))
# print(numar_secret)
# while numar_secret > numar_ales:
#     print('Nr secret e mai mare')
#     numar_secret += numar_ales
#     break
# print(numar_secret)

# correct_guess=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess = int(input('Guess a number: '))
#     guess_count += 1
#     if guess == correct_guess:
#         print('Congratulations! You won!')
#         break
# else:
#     print('sorry you lost')

# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = 0
# while numar_ghicit < numar_secret:
#     numar_ales = int(input('Alege un numar: '))
#     numar_ghicit +=1
#     if numar_ales < numar_secret:
#         print('Nr secret e mai mare')
#         break
#     elif numar_ales > numar_secret:
#         print('Nr secret e mai mic')
#         break
#     else:
#         print('Felicitări! Ai ghicit!')
# print(numar_secret)

# 4.
# numar = int(input('Alege un numar: '))
# nr = 0
# while nr == numar:
#     print()
# rows = int(input("Enter number of rows: "))
#
# ascii_value = 65
#
# for i in range(rows):
#     for j in range(i + 1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")
#
#     ascii_value += 1
#     print("\n")

# numar = int(input('Alege un numar: '))
# nr = 1
# for i in range(numar):
#     for n in range(i + 1):
#         cifra = int(nr)
#         print(cifra, end='')
#     nr += 1
#     print('\n')
