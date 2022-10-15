# ASSIGNMENT SESSION 4
# MADE WITH 💙 BY SAEPUL BAHRI (TI221 - INFORMATICS ENGINEERING)

def find_the_price():
    init_price = int(input('Enter product inital price: '))

    new_price = init_price * (10 / 100) + init_price
    print(f"The new price is: {int(new_price)}")


find_the_price()
