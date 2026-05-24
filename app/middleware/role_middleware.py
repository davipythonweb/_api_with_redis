from functools import wraps

from flask import jsonify


def role_required(role):

    def decorator(f):

        @wraps(f)
        def decorated(*args, **kwargs):

            # futura validação de roles

            return f(*args, **kwargs)

        return decorated

    return decorator