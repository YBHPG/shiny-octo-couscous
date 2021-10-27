from typing import Dict
from pymysql import connect
from pymysql.err import InterfaceError, OperationalError


class UseDatabse:
    # инициализация конфигурации
    def __init__(self, config: Dict):
        self.config = config

    # создание подключения к базе и проверка ошибок
    def __enter__(self):
        try:
            self.connection = connect(**self.config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except InterfaceError as err:
            return err
        except OperationalError as err:
            if err.args[0] == 1049:
                print('Неверное название базы данных\n')
            if err.args[0] == 1045:
                print('Неверное имя пользователя или пароль\n')
            if err.args[0] == 2003:
                print('Неверное имя хоста\n')
            return None

    # завершение работы с базой
    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_value is None:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        elif exc_value == 'cur':
            print('Курсор не создан\n')
        elif exc_value.args[0] == 1046:
            print('Неправильный синтаксис SQL запроса\n')
        elif exc_value.args[0] == 1146:
            print('Неправильное название таблицы\n')
        elif exc_value.args[0] == 1054:
            print('Неправильное название поля\n')
        return True

    # запуск работы функций получения данных из базы

    def work_with_db(config: Dict, sql: str):
        with UseDatabse(config) as cursor:
            if cursor is None:
                raise ValueError('is None')
            cursor.execute(sql)
            schema = [column[0] for column in cursor.description]
            result = []
            for row in cursor.fetchall():
                result.append(dict(zip(schema, row)))
            return result
