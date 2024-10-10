from random import randint
choice = randint(1,10)

print(f'Your choice is {choice}')

if choice == 7:
    print('Lucky')
else:
    print('Unlucky')