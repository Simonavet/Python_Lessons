from deimportat23 import TestCase1, TestCase2, TestCase3
import math # se cauta dupa modulul built-in (buit-in => in interiorul python) math apelandu-se functia import() <=>  __import__() si daca nu se gaseste, vom avea o eroare
# modul python = un fisier care contine definitii si statements python, adica, functii, clase, variabile

from math import *
print(pi)
print(factorial(6))

from math import pi
print(pi)


pie = math.pi
print("The value of pi is : ",pie)

child1 = TestCase1()
child2 = TestCase2()
child3 = TestCase3('test_case_nr_0003', 'the test case validate the design and functionality of [OK] button')
child1.test_exe()
child2.test_exe()
print(child3.get_name())
print(child3.get_summary())
child3.test_exe()
child3.runTwice()





