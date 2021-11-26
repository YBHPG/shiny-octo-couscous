from functools import wraps
from flask import session, request, current_app


def group_permission_validation():
    access_config = current_app.config['ACCESS_CONFIG']
    group_name = session.get('user_group_name', 'unauthorized')
    if len(request.endpoint.split('.')) == 1:
        target_app = ""
    else:
        target_app = request.endpoint.split('.')[0]
    if group_name in access_config and target_app in access_config[group_name]:
        return True
    return False


def group_permission_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_permission_validation():
            return f(*args, **kwargs)
        return 'Доступ запрещен'

    return wrapper


def query_permission_validation():
    access_config = current_app.config['ACCESS_QUERY_CONFIG']
    group_name = session.get('user_group_name', 'unauthorized')
    if len(request.endpoint.split('.')) == 1:
        target_app = ""
    else:
        target_app = request.endpoint
    if group_name in access_config and target_app in access_config[group_name]:
        return True
    return False


def query_permission_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if query_permission_validation():
            return f(*args, **kwargs)
        return 'Доступ запрещен'

    return wrapper
