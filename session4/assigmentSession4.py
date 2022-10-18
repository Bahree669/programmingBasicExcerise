# ASSIGNMENT SESSION 4
# MADE WITH 💙 BY SAEPUL BAHRI (TI22I - INFORMATICS ENGINEERING)

def get_product():
    product_name = input("Product name: (Enter '/' to close the form) ")

    if product_name == '/' or not product_name:
        return None

    product_price = float(input(f"{product_name.capitalize()} price: "))
    return {'name': product_name, 'price': product_price}


def find_the_price():
    products = []
    while True:
        product = get_product()
        if not product:
            break
        else:
            products.append(product)

    if not len(products):
        print('No products')
        return

    for product in products:
        p_name = product.get('name')
        p_price = product.get('price')

        new_price = p_price + (p_price * (10 / 100))

        print('===========================')
        print(f"Product name: {p_name}")
        print(f"{p_name.capitalize()} | "
              f"old price: {int(p_price)} | "
              f"new price: {int(new_price)}")


find_the_price()
