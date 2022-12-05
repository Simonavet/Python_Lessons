# Importare
class Test_case1:
    # metoda
    def printeaza_test_case(self):
        print('Running Test case 1')

class Test_case2:
    def printeaza_test_case(self):
        print('Running Test case 2')

class Test_case3:
    def __init__(self, name, summary):
        self.name = name # construim o proprietate de tip name
        self.summary = summary
    def return_name(self):
        return self.name
    def return_summary(self):
        return self.summary
    def printeaza_test_case(self):
        print('Running Test case 3')