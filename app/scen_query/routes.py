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


@query_app.route('/cost')
@query_permission_decorator
def get_work_by_date():
    cost = request.args.get('limit')
    if cost is None:
        return render_template('work_index.html')
    sql = provider.get('work.sql', cost=cost)
    db_config = current_app.config['DB_CONFIG']
    result = work_with_db(db_config, sql)

    context = {'schema': ['№', 'Наименование', 'Стоимость'], 'data': result}

    return render_template('work_list.html', context=context)


@query_app.route('/date')
@query_permission_decorator
def get_orders_by_date():
    begin = request.args.get('begin')
    end = request.args.get('end')
    if begin is None or end is None:
        return render_template('order_index.html')
    sql = provider.get('order.sql', begin=begin, end=end)
    db_config = current_app.config['DB_CONFIG']
    result = work_with_db(db_config, sql)

    context = {'schema': ['№', 'Клиент', 'Дата выполнения ремонта',
                          'Общая стоимость ремонта'], 'data': result}

    return render_template('order_list.html', context=context)
