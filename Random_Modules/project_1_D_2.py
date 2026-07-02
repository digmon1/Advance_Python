from random import *
import time
player1='Ronaldo'
player2='Messi'
player3='Halland'
player4='Mbappe'
r=m=h=o=0
print()
print("Welocome to our Racing game!....")
print("--"*40)
while True:
    n=randint(1,6)
    print(f'{player1}: {n}')
    r+=n
    time.sleep(2)

    n=randint(1,6)
    print(f'{player2}: {n}')
    m+=n
    time.sleep(2)

    n=randint(1,6)
    print(f'{player3}: {n}')
    h+=n
    time.sleep(2)

    n=randint(1,6)
    print(f'{player4}: {n}')
    o+=n
    time.sleep(2)

    if r>=20 and r>m and r>h and r>o:
        print(f'Congratulations!!! {player1} you have won')
        break

    if m>=20 and m>r and m>h and m>o:
        print(f'Congratulations!!! {player2} you have won')
        break

    if h>=20 and h>m and h>r and h>o:
        print(f'Congratulations!!! {player3} you have won')
        break

    if o>=20 and o>m and o>h and o>r :
        print(f'Congratulations!!! {player4} you have won')
        break
    else:
        pass
    print("--"*40)
    print()