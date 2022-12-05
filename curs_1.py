import keyword
# asa adaugam comnetarii
# '''
# asa se mai poate comenta
# pe mai multe
# randuri
# multiple line
# '''
# ""
# # alta metoda cand avem un bloc
# # adghj
# # afkghg
# ""
# print('Salutari1')
# print() # new line
# print('\n') # new line
# print('')
# print("")
# print("Salutari2")
# print('Hello world!')
# print('o----/')
# print(' ||||')
# print('*'*20)
# print('Hello World!', 'test', 'test1')
# print('Hello World!', 'test', 'test1', sep='-') #separator intre stringuri
# print('Hello World!', 'test', 'test1', end='@') # cum sa termine sirul
# print('Hello2')
# print('Hello3')
# #de afisat caractere speciale
# print('Hello! My planet is "earth"')
# print('Hello! My planet is \'earth\'')

#VARIABILE = O ADRESA DE MEMORIE IN CARE STOCAM INFORMATII
myVarFirstSecond = 3 # camel case
my_var_first = 3 # snake case
#declararea sa nu inceapa cu numere sau caractere speciale, se poate la sfarsit sau keywoeduri specifice
my_var_first1 = 3
print('The list of python keywords is:')
print(keyword.kwlist)
#suprascriere
my_var_first1 = True
my_var_first1 = 3
my_var_first1 = 'test'
print(my_var_first1)
#declarare si initializare multipla
var1, var2, var3, var4 = 'c', True, 34, 'complet'
print(var1)
print(var3)
print(var2)
print(var4)
var= va = va1 = va2 = 'c'
print(var)
print(va)
#concatenare
var1 = 'adela'
var2 = 'alexa'
print('Numele meu este: ' + var2 + ' si prenumele este: ' + var1)
print('Numele meu este:' + ' ' + var2 + ' si prenumele este: ' + var1)
#concatenare de doua tipuri de date diferite
var1 = 'Adela'
var2 = False
#type casting
var1 = 'Adela'
var2 = False
var3 = 33
var4 = 1.67
print('Adela')
print(var1)
print(str(var1))
print(str(var2))
# print('varsta mea este: ' + var3) #eroare
print('varsta mea este: ' + str(var3))
pretBanane = '5'
pretCartofi = '4'
# print('Pretul final de plata la casa: ', pretBanane + pretCartofi) #eroare
# print('Pretul final de plata la casa: ', int(pretBanane) + pretCartofi)
# variabila_bool_True = True
# variabila_bool_False = False
# print(variabila_bool_False)
# print(variabila_bool_True)
variabila_float = 1.67
variabila_int = 13
print(float(variabila_int))
print(int(variabila_float))
#formatare
# # print(f{})
# var1 = 'test'
# var2 = 13
# var3 = True
# var4 = 1.07
print(f'prima variabila are valoarea {var1}, a doua variabila are val {var2}, apoi {var3} si in final {var4}')
#
# #tipuri de date = ce tip de info este alocat la adresa de memorie
# #numerice = int, float, complex
# var = 2 + 3j # complex
# print(var)
# var1 = 3
# var2 = 3.6
# # boolean True si False
# #seaquals type = string,
# #lista = colectie de date diferite in paranteze patrate
# #tuple = colectie de date diferite in paranteze rotunde => imutabil
# mytuple = ('hello', 23, true)
# #set = colectie care tipuri neorodnabile care nu suporta duplicate
# mySet = set(77, True, True, 3, 5, 2-7j)
# print(mySet)
# #dict
#functia type sa aflam ce tip de date am folosit
#type se poate folosi cu type casting
#assert = modalitate prin care facem comparatie si decidem daca sistemul functioneaza sau nu
imi_place_la_curs = True
assert imi_place_la_curs == True "Error, error: studenti plictisiti "
print('Yey, fac treaba buna')
#input - valori de la tastatura


