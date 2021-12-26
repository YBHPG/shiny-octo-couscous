from datetime import datetime
from flask import Blueprint, render_template, request, session, current_app
from werkzeug.utils import redirect
from sql_provider import SQLProvider
import os
from .utils import add_to_cart, clean_cart
from access import login_permission_required

from usedatabase import update_db, work_with_db


cart_app = Blueprint('cart', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(
    os.path.dirname(__file__), 'sql'))


@cart_app.route('/', methods=['GET', 'POST'])
@login_permission_required
def cart_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        current_cart = session.get('cart', [])
        sql = provider.get('order_list.sql')
        items = work_with_db(db_config, sql)
        print(items)
        return render_template('cart_order_list.html', items=items, cart=current_cart)
    else:
        product_id = request.form['product_id']
        sql = provider.get('order_item.sql', product_id=product_id)
        items = work_with_db(db_config, sql)
        if not items:
            return 'Items not fount'
        add_to_cart(items[0])
        return redirect('/cart')


@cart_app.route('/buy')
@login_permission_required
def buy_cart():
    current_cart = session.get('cart', [])
    if current_cart:
        for product in current_cart:
            total_cost = int(product['unit_cost']) * int(product['number'])
            sql = provider.get('insert_cart.sql', product_code=product['product_id'],
                               ordered_number=product['number'],
                               order_date=datetime.now(),
                               user_id=session['user_id'],
                               cart_amount=product['number'],
                               total_cost=total_cost)
            update_db(current_app.config['DB_CONFIG'], sql)
            print('SQL:' + str(sql))
            clean_cart()
        return render_template('buy_success.html')
    return redirect('/cart')


@cart_app.route('/clear')
def clear_cart_handler():
    clean_cart()
    return redirect('/cart')
