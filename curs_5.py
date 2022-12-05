# for each
# parcurgeti lista si daca intalnim soarece il stergem
# animale = {'cal', 'pisica', 'caine', 'magar', 'soarece', 'oaie', 'vaca'}

# for animal in animale:
#     if animal == 'soarece':
#         animale.remove(animal)
# print(animale)

# nu putem folosi pop() deoarece functia pop ia ca si parametru indexul

# la structuri repetitive se poate folosi si "else"

# for else
# printati toate elementele pana la 5
# for i in range(6):
#     print(i)
# else:
#     print('am terminat')
#
# # while - else
# i = 0
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print('Am terminat')

# else este optionala si se executa o singura data la final

# Functii
# modalitate prin care economisim cod
# o folosim o singura data si putem face apel la functie cand e nevoie
# intotdeauna se face cu "def"
# poate avea parametri sau nu
# dupa def, si nume functie obligatoriu punem paranteze
# trebuie sa aiba un nume sugestiv
# parametri = info de care f are nevoie din exterior pt e putea executa instructiunile - intre paranteze ()
# trebuie sa aiba optiune de return = keyword "return"
# indentarea corpul f marcat de indentarea fata de marginea fisierului

# 1. Functii simple = fara parametri
def print_noapte_buna():
    print('Noapte buna') # corpul functiei - actiunea ce trebuie facuta
    print('Este ora 8')
# print_noapte_buna() # chemarea functiei - nu ruleaza fara
# print_noapte_buna()
# print_noapte_buna()
# print_noapte_buna()

# x = print_noapte_buna() # punem intr-o variabila rezultatul executiei
# print(x)
# da none pt ca nu i-am dat return

# def print_noapte_buna1():
#     print('Noapte buna')
#     print('Este ora 8')
#     msg = 'sunt obosit'
#     return msg
# y = print_noapte_buna1()
# print(y)

# exercitiu: suma a doua numere
# calculeaza_suma() daca apelam inainte de definire da eroare trebuie mai inatai definita si apoi apelata
def calculeaza_suma():
    a = 3
    b = 4
    suma = a + b
    print(f'Suma celor doua numere este {suma}')
    return suma

calculeaza_suma()
x = calculeaza_suma()
print(x)
# x ia valoarea returnata

# 2. Functii cu parametri
# intre () se specifica numele informatiei ce trebuie parametrizata
# def suma(a,b):
#     sum = a+b
#     print(f'Suma celor 2 nr este {sum}')
#     return sum
#
# # suma(2,4)
# # x = suma(2,4)
# # print(x)
#
# suma(3,5)
# suma(4) tot timpul la apel trebuie sa aiba acelasi numar de parametri definiti

# calculeaza pretul unui bilet
# fctie cu numar indefinit de parametrii
# def calculeaza_pretul(*nr):
#     pret = 0
#     for element in nr:
#         pret = pret + element
#     return pret
# print(calculeaza_pretul(2, 6, 7))
# print(calculeaza_pretul(1,3))
# print(calculeaza_pretul(1,3,6, 4, 7,8,9))
# print(calculeaza_pretul('casa', 'masina')) - daca dam int tot timpul punem int nu merge cu string
