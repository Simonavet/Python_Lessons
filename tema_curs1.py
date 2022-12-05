# masina_de_spalat = 'Arctic'
# garantie_luni = 48
# pret = 1199.99
# cumparam = True
#
# print(type(masina_de_spalat))
# print(type(garantie_luni))
# print(type(pret))
# print(type(cumparam))
#
# print(round(pret))
# pret = 1200.00
# print(type(pret))
#
# print(f'Ca dorim sa cumparam o masina de spalat haine marca:', masina_de_spalat , 'cu garantie de' , garantie_luni , 'luni in valoare de' , pret , 'lei e' , cumparam,'.')
# specie = 'caine'
# varsta = 2
# temperatura = 37.5
# sanatate = True
# print(f'Avem un' , specie , 'de' , varsta , 'ani cu temperatura de', temperatura , 'grade Celsius. E' , sanatate , 'ca e sanatos.')
#
# planta = 'ficus'
# varsta_planta = 4
# lungime = 220.50
# are_loc = False
# print('Acest copac de' , planta , 'in varsta de' , str(varsta_planta) , 'ani cu o lungime de' , str(lungime) , 'cm e' , str(are_loc) , 'ca are loc.')
#
# obiect = 'creion'
# lungimeCreion = 20
# tipMina = 0.7
# scrie = False
# print(f'Acest' , obiect , 'de lungime' , lungimeCreion , 'cm, cu mina de' , tipMina , 'e' , scrie , 'ca e bun.')
#
# nume = input('Scrie numele aici:')
# prenume = input('Scrie si prenumele, te rog:')
# print('Numele complet are' , len(nume + prenume) , 'caractere')
#
# lungimea = int(input('Care este lungimea?'))
# latimea = int(input('Care este latimea?'))
# print('Aria dreptunghiului este' , lungimea*latimea,'.')
#
# string = 'Coral is either the stupidest animal or the smartest rock'
# print(string.count(' the '))
# string.count(' the ')
#
# def count_occurrences(string):
#     return string.lower().split().count(' the ')
# result = string.split()
# print(result)
# print("The total number of words is: "  + str(len(result)))
# print(str(result.count('the')))
#
# var1 = False
# assert var1== True, "Error, error: studenti plictisiti"
# print('Fac treaba buna la curs')
#
# string = 'Coral is either the stupidest animal or the smartest rock'
# assert string == int(string), "Error, error: nu are numere"
# print('Are doar cuvinte')
# # Initialising string
# ini_string1 = '1234556'
# ini_string2 = 'ab123bc'
#
# # printing initial string
# print("Initial Strings : ", ini_string1, ini_string2)
#
# # Using isdigit()
# if ini_string1.isdigit():
#     print("String1 contains all numbers")
# else:
#     print("String1 doesn't contains all numbers")
#
# if ini_string2.isdigit():
#     print("String2 contains all numbers")
# else:
#     print("String2 doesn't contains all numbers")
#
# string = 'Coral is either the stupidest animal or the smartest rock'
# if string.isdigit():
#     print('String are doar numere')
#     assert string==string.isdigit(), "Error: Are numere."
# else:
#     print('Nu are numere')
#     assert string == string.isdigit(), "Error: Are doar litere."
#
# string1 = str(input('Scrie un cuvant de dimensiune impara'))
# print(string1.getMiddle)
# string1 = input('Scrie un string de lungime impara: ')

# def printMiddleCharacter(string1):
#     length = len(string1)
#     middle = length // 2
#     print(string1[middle])
# string1 = input('Scrie un string de lungime impara: ')
# printMiddleCharacter(string1)


# def printMiddleCharacter(str):
#     # Finding string length
#     length = len(str);
#
#     # Finding middle index of string
#     middle = length // 2;
#
#     # Print the middle character
#     # of the string
#     print(str[middle]);
#
#
# # Driver Code
#
# # Given string str
# str = "GeeksForGeeks";
#
# # Function Call
# printMiddleCharacter(str);

# propozitie = 'Vin acasa acum'
# if propozitie == propozitie[::-1]:
#     print('Este palindrom')
#     assert propozitie == propozitie[::-1] , "Error: Nu este la fel si invers"
# else:
#     print('Nu este palindrom')
#     assert propozitie == propozitie[::-1], "Error: Nu este la fel si invers"

pret = 1199.99
print(round(pret))
pret = round(pret)
print(type(pret))

'''If - else evalueaza conditii si bifurca codul in functie de rezultat.
De exeplu, daca suntem in Cluj si vrem sa ajungem la Turda,
cautam indicatorul care ne arata directia spre Turda.
Suntem pe o strada in linie dreapta si ajungem la o intersectie, vedem indicatorul ca arata drumul spre stanga, deci o luam la stanga.
Nu vedem niciun indicator, mergem mai departe pana il gasim si apoi o luam in directia scrisa pe tablita.
Nu vedem niciun indicator, deloc, mergem mai departe pana iesim din Cluj.'''