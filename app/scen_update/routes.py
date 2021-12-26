from flask import Blueprint, request, render_template, current_app, redirect
from sql_provider import SQLProvider
from usedatabase import work_with_db, update_db
from datetime import datetime

update_app = Blueprint('update', __name__, template_folder="templates")
provider = SQLProvider('scen_update/sql')


@update_app.route('/', methods=['GET', 'POST'])
def print_and_delete():
    if request.method == 'GET':
        items = work_with_db(
            current_app.config['DB_CONFIG'], provider.get('print.sql'))
        print(items)
        return render_template('update_index.html', items=items, heads=['id', 'Товар', 'Стоимость', ' '])
    else:
        product_id = request.form['product_id']
        sql = provider.get('delete.sql', product_id=product_id)
        update_db(current_app.config['DB_CONFIG'], sql)
        return redirect('/update')


@update_app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        product_name = request.form.get('product_name')
        product_category = request.form.get('product_category')
        unit_cost = request.form.get('unit_cost')
        now = datetime.now()
        if product_category and product_name and unit_cost:
            sql = provider.get('insert.sql', product_name=product_name,
                               product_category=product_category, unit_cost=unit_cost, quantity_fix_date=now)
            print(sql)
            update_db(current_app.config['DB_CONFIG'], sql)
            return redirect('/update')
        return 'Error'
