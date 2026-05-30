from app.extensions import db

from app.models.user_model import User

from app.utils.password import (
    hash_password,
    verify_password
)

from app.services.token_service import (
    generate_access_token,
    generate_refresh_token
)

from app.services.redis_service import (
    save_refresh_token
)

from app.services.user_service import (
    get_user_by_username,
    get_user_by_email
)


def register_user(data):

    username = data['username']
    email = data['email']
    password = data['password']

    # verificar username
    user_exists = get_user_by_username(username)

    if user_exists:
        return {
            'error': 'Usuário já existe'
        }

    # verificar email
    email_exists = get_user_by_email(email)

    if email_exists:
        return {
            'error': 'Email já cadastrado'
        }

    # criar usuário
    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.session.add(user)
    db.session.commit()

    return {
        'message': 'Usuário criado com sucesso'
    }


def login_user(data):

    username = data['username']
    password = data['password']

    user = get_user_by_username(username)

    if not user:
        return {
            'error': 'Usuário inválido'
        }

    password_valid = verify_password(
        password,
        user.password
    )

    if not password_valid:
        return {
            'error': 'Senha inválida'
        }

    access_token = generate_access_token(user)

    refresh_token = generate_refresh_token(user)

    # salvar refresh token no redis
    save_refresh_token(
        user.id,
        refresh_token
    )

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': user.to_dict()
    }