import os
from dotenv import load_dotenv

# carregar variáveis .env
load_dotenv()


class Config:

    # flask
    SECRET_KEY = os.getenv('SECRET_KEY')

    # jwt
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    REDIS_DB = os.getenv('REDIS_DB')

    # jwt expiração
    JWT_ACCESS_TOKEN_EXPIRES = 120