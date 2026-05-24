from flask import Blueprint

from flask_jwt_extended import (
    get_jwt_identity
)

from app.middleware.jwt_middleware import (
    jwt_required_custom
)

from app.services.user_service import (
    get_user_by_id
)

from app.utils.responses import (
    success_response
)


user_bp = Blueprint(
    'user',
    __name__
)


@user_bp.route('/profile', methods=['GET'])
@jwt_required_custom
def profile():

    user_id = get_jwt_identity()

    user = get_user_by_id(user_id)

    return success_response(
        'Usuário encontrado',
        user.to_dict()
    )