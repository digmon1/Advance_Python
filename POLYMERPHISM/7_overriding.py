class Father:
    def arrangement(self):
        print('Marriage Arrangement Successfully Done')

    def demand(self):
        print('Gold/Car/Cash/Others')
    def marry(self):
        print('Married to Kajal')

class Son(Father):
    def marry(self):
        print('Married to Katrina')
s=Son()
s.arrangement()
s.demand()
s.marry()