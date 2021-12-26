from flask import Blueprint, request, render_template, current_app

from sql_provider import SQLProvider
from usedatabase import work_with_db
from access import login_permission_required

query_app = Blueprint('query', __name__, template_folder='templates')

provider = SQLProvider('scen_query/sql')


@query_app.route('/')
@login_permission_required
def get_bp_index():
    return render_template('request_menu.html')


@query_app.route('/query1')
@login_permission_required
def query1():
    month = request.args.get('month')
    year = request.args.get('year')
    user_id = request.args.get('user_id')
    if month is None or user_id is None or year is None:
        return render_template('query1_index.html')
    sql = provider.get('query1.sql', month=month, year=year, user_id=user_id)
    result = work_with_db(current_app.config['DB_CONFIG'], sql)
    print(result)
    context = {'schema': ['ID Пользователя',
                          'Общая сумма покупок'], 'data': result}
    return render_template('query_result.html', context=context)


@query_app.route('/query2')
@login_permission_required
def query2():
    product_id = request.args.get('product_id')
    if product_id is None:
        return render_template('query2_index.html')
    sql = provider.get('query2.sql', product_id=product_id)
    result = work_with_db(current_app.config['DB_CONFIG'], sql)
    context = {'schema': ['ID товара на складе', 'Категория', 'Название',
                          'Материал', 'Единица измерения', 'Стоимость единицы товара',
                          'Количество на складе', 'Забронированное количество'], 'data': result}

    return render_template('query_result.html', context=context)


@query_app.route('/query3')
@login_permission_required
def query3():
    month = request.args.get('month')
    year = request.args.get('year')
    if month is None or year is None:
        return render_template('query3_index.html')
    sql = provider.get('query3.sql', month=month, year=year)
    result = work_with_db(current_app.config['DB_CONFIG'], sql)
    context = {'schema': ['ID заказа', 'ID пользователя', 'Дата заказа',
                          'Заказанное количество', 'Общая стоимость заказа',
                          'Статус', 'ID товара'], 'data': result}

    return render_template('query_result.html', context=context)


@query_app.route('/query4')
@login_permission_required
def query4():
    payment_document_id = request.args.get('payment_document_id')
    if payment_document_id is None:
        return render_template('query4_index.html')
    sql = provider.get('query4.sql', payment_document_id=payment_document_id)
    db_config = current_app.config['DB_CONFIG']
    result = work_with_db(db_config, sql)

    context = {'schema': ['ID платёжного документа', 'Дата создания',
                          'Сумма покупок', 'Количество позиций'], 'data': result}

    return render_template('query_result.html', context=context)
