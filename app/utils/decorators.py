from functools import wraps
from flask import jsonify


def admin_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        # futura lógica de permissão admin

        return f(*args, **kwargs)

    return decorated