#operatorii de atribuire = , += , -= , *= , /=
# =
variabila1 = 7
variabila1 = 53
# +=
# variabila1 += 7 # adauga 7 la 53 => 60
# print(variabila1)
variabila1 = variabila1 + 7
print(variabila1)
list1 = [1, 2, 3]
list2 = [4, 5]
print(id(list1), id(list2)) #locul din memorie
# list1+=list2
# print(list1)
# print(id(list1))
list1=list1+list2
print(list1)
print(id(list1)) #se aloca o noua zona de memorie
#-=
var2 = 47
var2 -=7
print(var2) # din valoarea anterioara scade valoarea 7 => var2
var2 = var2-7
print(var2)
# *= inmultire
var2 = 7
var2 *=7 # valoarea anterioara se va inmulti cu 7 iar rezultatul final => var2
print(var2)
var2 = var2*2
print(var2)
#/= impartire
var2 = 7
var2 /=7 # valoarea anterioara se va imparti la 7 iar rezultatul final => var2
print(type(var2))
var2 = var2/2
print(var2)

#operatori aritmetici: +, -, *, /, **, %, //
nr1 = 2
nr2 = 3
print(f'suma este ', nr1 + nr2)
print(f'dieferenta este {nr1 - nr2}')
print(f'produsul este {nr1 * nr2}')
print(f'impartirea este {nr1 / nr2}')
# % modulo - ne arata restul impartirii
print(f'restul este {nr1 % nr2}')

# // floor division - ne arata doar catul, ne taie zecimalele
print(f'rezultatul este {nr1 // nr2}')

# ** ridicare la putere
print(f'puterea este {nr1 ** nr2}')

#operatori de comparatie: ==, <=, >=, <,>, != (diferit)
# returneaza un rezultat boolean
# nr1 = 5
# nr2 = 6
# print(nr1 == nr2)
# print(nr1 <= nr2)
# print(nr1 >= nr2)
# print(nr1 < nr2)
# print(nr1 > nr2)
# print(nr1 != nr2)

#operatorii logici - and, or, not
# and - strict
# not - opusul rezultatului conditiei
# ordinea prioritatilor: not > and > or
nr1 = 5
nr2 = 6
print(nr1 > nr2 or nr1==nr2) # false or false => false
print(nr1 > nr2 or nr1<nr2) # False or True => True
print(nr1 > nr2 and nr1<nr2) # False and True => False
print(not nr1 > nr2 and nr1 < nr2) # True and True => True
print(not(nr1>nr2 and nr1<nr2)) # not(False and True) => not(False) => True
print(not nr1 == nr2 and not nr1 >= nr2) # not False and not False => True


