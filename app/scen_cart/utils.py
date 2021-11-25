from flask import session


def add_to_cart(items):
    cart = session.get('cart', [])
    for item in items:
        cart.append(item)
    print(cart)
    session['cart'] = cart


def clean_cart():
    cart = session.get('cart', [])
    if cart:
        session.pop('cart')
