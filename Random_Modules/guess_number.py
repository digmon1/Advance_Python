from random import *
print()
print("Welcome to our guessing number Application!!!....")
print("--"*30)
attempt = 0
n=randint(1,100)
while True:
    guess=int(input('Enter your guess..[1-100]: '))

    if guess == n:
        attempt=attempt+1
        print(f"Congratulations!!! you have guessed it correctly in {attempt} times")
        break
    elif guess<n:
        print('Value is greater ...')
        attempt+=1
    else:
        print('Value is Less...')
        attempt=attempt+1
    print("--"* 30)
    print()
