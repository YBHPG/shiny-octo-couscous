from flask import Blueprint, request, render_template, current_app

from sql_provider import SQLProvider
from usedatabase import work_with_db
from access import group_permission_decorator, query_permission_decorator

query_app = Blueprint('query', __name__, template_folder='templates')

provider = SQLProvider('scen_query/sql')


@query_app.route('/')
@group_permission_decorator
def get_bp_index():
    return render_template('request_menu.html')


@query_app.route('/query1')
@query_permission_decorator
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
    return render_template('query1_result.html', context=context)


@query_app.route('/query2')
@query_permission_decorator
def query2():
    product_id = request.args.get('product_id')
    if product_id is None:
        return render_template('query2_index.html')
    sql = provider.get('query2.sql', product_id=product_id)
    result = work_with_db(current_app.config['DB_CONFIG'], sql)
    context = {'schema': ['ID товара на складе', 'Категория', 'Название',
                          'Материал', 'Единица измерения', 'Стоимость единицы товара',
                          'Количество на складе', 'Забронированное количество'], 'data': result}

    return render_template('query2_result.html', context=context)


@query_app.route('/cost')
@query_permission_decorator
def query3():
    cost = request.args.get('limit')
    if cost is None:
        return render_template('query3_index.html')
    sql = provider.get('work.sql', cost=cost)
    db_config = current_app.config['DB_CONFIG']
    result = work_with_db(db_config, sql)

    context = {'schema': ['№', 'Наименование', 'Стоимость'], 'data': result}

    return render_template('query3_result.html', context=context)


@query_app.route('/cost')
@query_permission_decorator
def query4():
    cost = request.args.get('limit')
    if cost is None:
        return render_template('query4_index.html')
    sql = provider.get('work.sql', cost=cost)
    db_config = current_app.config['DB_CONFIG']
    result = work_with_db(db_config, sql)

    context = {'schema': ['№', 'Наименование', 'Стоимость'], 'data': result}

    return render_template('query4_result.html', context=context)
