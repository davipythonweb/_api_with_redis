from app.database.redis_client import redis_client


def save_refresh_token(user_id, refresh_token):

    redis_client.set(
        f'refresh_token:{user_id}',
        refresh_token,
        ex=604800
    )


def get_refresh_token(user_id):

    return redis_client.get(
        f'refresh_token:{user_id}'
    )


def delete_refresh_token(user_id):

    redis_client.delete(
        f'refresh_token:{user_id}'
    )