# MADE WITH 💙💛 BY SAEPUL BAHRI (TI22I - INFORMATICS ENGINEERING - 20220040277)
from sys import platform
import os
from time import sleep

initial_products = [
    {'name': 'jeans', 'price': 100000, 'stock': 100, 'margin': 50},
    {'name': 'shirt', 'price': 85000, 'stock': 30, 'margin': 30},
    {'name': 'blouse', 'price': 200000, 'stock': 200, 'margin': 40},
    {'name': 'dress', 'price': 350000, 'stock': 50, 'margin': 30},
]
products = [
    {'name': 'jeans', 'price': 100000, 'stock': 100, 'margin': 50},
    {'name': 'shirt', 'price': 85000, 'stock': 30, 'margin': 30},
    {'name': 'blouse', 'price': 200000, 'stock': 200, 'margin': 40},
    {'name': 'dress', 'price': 350000, 'stock': 50, 'margin': 30},
]
order_history = []
profit = []


def display_menu():
    navigations = [
        '-h -> open help',
        'add -> add product',
        'buy -> buy product',
        'close -> close app',
        'clear -> clear display',
        'stock -> show products',
        'diff - see your profit'
    ]

    print('------------------------')
    for menu in navigations:
        print(menu)
    print('------------------------')


def display_error_input(input):
    print(f"Command '{input}' is unrecognized by system. Enter -h for help.")


def display_products(products, show_margin):
    if show_margin:
        print('------------------------------------------------------------')
        print("{:<15} {:<20} {:<10} {:<20}".format(
            'Product Name', 'Price', 'Stock', 'Price Margin'))
        print('------------------------------------------------------------')

        # display the products in tubular format
        for p in products:
            print("{:<15} {:<20} {:<10} {:<20}".format(
                p['name'], f"Rp {int(p['price'])}", p['stock'], p['margin']))
        print('------------------------------------------------------------')
    else:
        print('------------------------------------------')
        print("{:<15} {:<20} {:<10}".format(
            'Product Name', 'Price', 'Stock'))
        print('------------------------------------------')

        # display the products in tubular format
        for p in products:
            print("{:<15} {:<20} {:<10}".format(
                p['name'], f"Rp {int(p['price'])}", p['stock']))
        print('------------------------------------------')


def clear_display():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('cls')
    elif platform == "win32":
        os.system('cls')


# return a list of products
def add_product():
    products_data = []

    while True:
        print('-------------------------')
        print('➕ ADD PRODUCT ➕')
        print('-------------------------')

        p_name = input('Product name: ').lower()
        p_price = float(input('Product price: '))
        p_stock = int(input('Product stock: '))
        p_margin = int(input('Product price margin: '))

        print('-------------------------')
        # append data product to 'products'
        products_data.append(
            {'name': p_name, 'price': p_price, 'stock': p_stock, 'margin': p_margin})

        # append the product_data to products
        for p in products_data:
            initial_products.append(p)
            products.append(p)

        # remove inputed product data
        products_data.clear()

        # ask the user if they want to close the form
        close_form = input('Finish adding product? Y or N ').lower()
        if close_form == 'y':
            display_products(products=products, show_margin=True)
            print('Returning to home...')
            sleep(3)
            clear_display()
            break


def buy_product():
    def find_product_idx(name):
        for idx, p in enumerate(products):
            if p['name'] == name:
                return idx
        return -1

    def validate_amount(p_amount, p_index):
        p_stock = products[p_index]['stock']
        return p_stock - p_amount > -1

    while True:
        # exit if there are no items in 'products'
        if not len(products):
            print('There are no products.\nReturning to home...')
            sleep(2)
            clear_display()
            break
        else:
            display_products(products=products, show_margin=False)

        # get user order
        p_name = input('Product name: ').lower()
        p_index = find_product_idx(name=p_name)

        if p_index > -1:
            p_amount = 1
            amnt_is_valid = True

            while amnt_is_valid:
                p_amount = int(input('Product ammount: '))

                amnt_is_valid = validate_amount(
                    p_amount=p_amount, p_index=p_index)
                # substract the product stock by p_amount only if p_amount <= stock
                if amnt_is_valid:
                    products[p_index]['stock'] -= p_amount
                    break
            else:
                print("The amount of product you're going to buy is too high.")
                p_amount = 1

            # calculate order
            p_price = products[p_index]['price']
            p_margin = products[p_index]['margin']

            order_profit = p_amount * (p_price + (p_price * (p_margin / 100)))

            profit.append(order_profit)

            order_history.append({'name': p_name, 'price': p_price, 'amount': p_amount, 'margin': str(
                p_margin) + '%', 'total': int(order_profit)})

        else:
            print(f'Cannot find item with name of {p_name}')

        continue_shopping = input('Continue shopping? Y or N ').lower()
        if continue_shopping == 'n':
            print_receipt()
            break


def print_receipt():
    profit_sum = sum(profit)

    print('==============================================================')
    print('ORDER RECEIPT')
    print('==============================================================')
    print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(
          'Product Name', 'Price', 'Amount', 'Margin', 'Total'))
    print('--------------------------------------------------------------')

    # display the products in tubular format
    for p in order_history:
        print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(
            p['name'], f"Rp {int(p['price'])}", p['amount'], p['margin'], f"Rp {int(p['total'])}"))
    print('--------------------------------------------------------------')

    print(f'Total profit: Rp {int(profit_sum)}')
    print('--------------------------------------------------------------')


def diff():
    if len(initial_products) and len(order_history):
        print('INITIAL STOCKS')
        display_products(products=initial_products, show_margin=True)

        print('CURRENT STOCKS')
        display_products(products=products, show_margin=True)

        print('ORDER HISTORY')
        print_receipt()
    else:
        print("You haven't order anything yet.")


def main():
    display_menu()

    while True:
        user_ctrl = input('> ').lower()

        clear_display()

        if user_ctrl == '-h':
            display_menu()
        elif user_ctrl == 'close':
            break
        elif user_ctrl == 'clear':
            clear_display()
        elif user_ctrl == 'add':
            add_product()
        elif user_ctrl == 'buy':
            buy_product()
        elif user_ctrl == 'stock':
            display_products(products=products, show_margin=True)
        elif user_ctrl == 'diff':
            diff()
        else:
            display_error_input(input=user_ctrl)


main()
