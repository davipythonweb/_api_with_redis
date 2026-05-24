from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)


def generate_access_token(user):

    return create_access_token(
        identity=user.id
    )


def generate_refresh_token(user):

    return create_refresh_token(
        identity=user.id
    )