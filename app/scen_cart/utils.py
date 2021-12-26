from flask import session


def add_to_cart(item):
    basket = session.get('cart', [])
    check = False
    for it in basket:
        if it['product_id'] == item['product_id']:
            check = True
            break

    if check:
        for it in basket:
            if it['product_id'] == item['product_id']:
                it['number'] += 1
    else:
        item['number'] = 1
        basket.append(item)
    session['cart'] = basket


def clean_cart():
    cart = session.get('cart', [])
    if cart:
        session.pop('cart')
