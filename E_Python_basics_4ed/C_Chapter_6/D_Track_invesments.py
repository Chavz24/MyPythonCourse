""" Challenge: Track Your Investments 6.5"""

# In this challenge, you will write a program called invest.py that tracks
# the growing amount of an investment over time.

def invest(amount,rate,years):
    """This Function tracks the grow of an amount over time"""

    for year in range(years):
        amount=amount+(amount*(rate/100))
        year+=1
        print(f'Al final del ano {year} el capital es de {amount:,.2f}.')

while True:
    try:
        user_amount=float(input('Ingrese una cantidad: '))
        break
    except:
        print('Ingrese una cantidad en numeros, por favor.')

while True:
    try:
        user_rate=float(input('Ingrese una tasa: '))
        break
    except:
        print('Ingrese una tasa en numeros, por favor.')

while True:
    try:
        user_years=int(input('Ingrese los anos: '))
        break
    except:
        print('Ingrese el ano en numero, por favor.')

invest(user_amount,user_rate,user_years)




