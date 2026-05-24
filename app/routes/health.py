from flask import Blueprint

from app.utils.responses import (
    success_response
)


health_bp = Blueprint(
    'health',
    __name__
)


@health_bp.route('/', methods=['GET'])
def health():

    return success_response(
        'API online'
    )