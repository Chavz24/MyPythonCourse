#usando logging para debuquar un programa

import random, logging
open('mylog.txt','w').write('\n')
logging.basicConfig(filename="mylog.txt",level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

guess = ''
options=('heads', 'tails')
logging.debug(f'heads{options.index("heads")} ,tails {options.index("tails")} Linea 8')

while guess not in options :
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(f'primer guess{guess}Linea 12')
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

logging.debug(f'toss={toss}Linea 14')
logging.debug(f'primer guess={options.index(guess)}Linea 15')
logging.debug(f'primer guess={options.index(guess)}= toss{toss} ? Linea 16')

if toss == options.index(guess):
    print('You got it!')
else:
    print('Nope! Guess again!')
    while True:
        guess = input()
        if guess in options:
            break
        else:
            print('Only options are heads or tails dummy')

    logging.debug(f'seg guess{guess}Linea 21')
    logging.debug(f' seg guess {options.index(guess)} Linea 22')
    logging.debug(f'seg guess={options.index(guess)}= toss{toss} ? Linea 16')

    if toss ==options.index(guess):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
