from functools import wraps

from flask import jsonify

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity
)

from app.services.user_service import (
    get_user_by_id
)


def jwt_required_custom(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        try:

            verify_jwt_in_request()

            user_id = get_jwt_identity()

            user = get_user_by_id(user_id)

            if not user:

                return jsonify({
                    'success': False,
                    'message': 'Usuário não encontrado'
                }), 404

        except Exception as e:

            return jsonify({
                'success': False,
                'message': str(e)
            }), 401

        return f(*args, **kwargs)

    return decorated