from random import *
s= ['Mango', 'Banana', 'Grapes', 'Apple', 'Orange','Pineapple','Cherry']
print(choice(s))
print(choices(s,k=3))
print(sample(s,k=5))
shuffle(s)
print(s)