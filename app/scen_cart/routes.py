from flask import Blueprint, request, redirect, current_app, render_template, session
from sql_provider import SQLProvider
from usedatabase import work_with_db, update_db
from .utils import add_to_cart, clear_cart

cart_app = Blueprint('cart', __name__, template_folder='templates')
provider = SQLProvider('scen_cart/sql')


@cart_app.route('/', methods=["GET", "POST"])
def cart_index():
    if request.method == "GET":
        current_cart = session.get('cart', [])
        sql = provider.get('cart_items.sql')
        items = work_with_db(current_app.config['DB_CONFIG'], sql)
        return render_template('cart_index.html', items=items, current_cart=current_cart)
    else:
        product_id = request.form['product_id']
        sql = provider.get('cart_check.sql', product_id=product_id)
        items = work_with_db(current_app.config['DB_CONFIG'], sql)
        if not items:
            return "Items not found"
        print(items)
        add_to_cart(items)
        return redirect('/cart')


@cart_app.route('/successful_purchase', methods=["GET", "POST"])
def buy():
    current_cart = session.get('cart', [])
    if current_cart:
        for product in current_cart:
            sql = provider.get('add_to_cart.sql', cart_product_id=product['product_id'],
                               cart_product_name=product['product_name'],
                               cart_product_category=product['product_category'],
                               cart_unit_cost=product['unit_cost'])
            update_db(current_app.config['DB_CONFIG'], sql)
        return render_template('successful_purchase')
    return redirect('/cart')


@cart_app.route('/clear', methods=["GET", "POST"])
def clear_cart():
    clear_cart()
    return redirect('/cart')
