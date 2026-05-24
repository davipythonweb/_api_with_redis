from flask import Blueprint
from flask import request

from app.schemas.login_schema import LoginSchema
from app.schemas.register_schema import RegisterSchema
from app.schemas.refresh_schema import RefreshSchema

from app.services.auth_service import (
    register_user,
    login_user
)

from app.utils.responses import (
    success_response,
    error_response
)

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token
)

from app.services.redis_service import (
    get_refresh_token
)


auth_bp = Blueprint(
    'auth',
    __name__
)

login_schema = LoginSchema()

register_schema = RegisterSchema()

refresh_schema = RefreshSchema()


@auth_bp.route('/register', methods=['POST'])
def register():

    errors = register_schema.validate(
        request.json
    )

    if errors:

        return error_response(
            errors,
            400
        )

    data = register_schema.load(
        request.json
    )

    result = register_user(data)

    if result.get('error'):

        return error_response(
            result['error'],
            400
        )

    return success_response(
        result['message'],
        status=201
    )


@auth_bp.route('/login', methods=['POST'])
def login():

    errors = login_schema.validate(
        request.json
    )

    if errors:

        return error_response(
            errors,
            400
        )

    data = login_schema.load(
        request.json
    )

    result = login_user(data)

    if result.get('error'):

        return error_response(
            result['error'],
            401
        )

    return success_response(
        'Login realizado com sucesso',
        result
    )


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():

    user_id = get_jwt_identity()

    refresh_token = request.json.get(
        'refresh_token'
    )

    redis_token = get_refresh_token(
        user_id
    )

    if refresh_token != redis_token:

        return error_response(
            'Refresh token inválido',
            401
        )

    new_access_token = create_access_token(
        identity=user_id
    )

    return success_response(
        'Novo access token gerado',
        {
            'access_token': new_access_token
        }
    )