from flask import jsonify
from functools import wraps

from app.database.redis_client import redis_client


def rate_limit(limit=10, seconds=60):

    def decorator(f):

        @wraps(f)
        def decorated(*args, **kwargs):

            ip = 'global'

            key = f'rate_limit:{ip}'

            current = redis_client.get(key)

            if current and int(current) >= limit:

                return jsonify({
                    'success': False,
                    'message': 'Limite de requisições excedido'
                }), 429

            pipe = redis_client.pipeline()

            pipe.incr(key, 1)

            pipe.expire(key, seconds)

            pipe.execute()

            return f(*args, **kwargs)

        return decorated

    return decorator