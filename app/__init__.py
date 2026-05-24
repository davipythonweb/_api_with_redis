from flask import Flask

from app.config.config import Config

from app.extensions import (
    db,
    jwt,
    ma,
    migrate
)

# importar blueprints
from app.routes.auth import auth_bp
from app.routes.user import user_bp
from app.routes.health import health_bp


def create_app():

    app = Flask(__name__)

    # carregar configurações
    app.config.from_object(Config)

    # iniciar extensões
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # registrar blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(health_bp, url_prefix='/health')

    return app