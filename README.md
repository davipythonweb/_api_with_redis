# _api_with_redis
Flaks api com jwt e Redis

app/
│
├── routes/
│   ├── auth.py
│   ├── user.py
│   └── health.py
│
├── middleware/
│   ├── jwt_middleware.py
│   ├── role_middleware.py
│   └── rate_limit.py
│
├── services/
│   ├── auth_service.py
│   ├── token_service.py
│   ├── user_service.py
│   └── redis_service.py
│
├── schemas/
│   ├── login_schema.py
│   ├── refresh_schema.py
│   ├── register_schema.py
│   └── user_schema.py
│
├── models/
│   └── user_model.py
│
├── database/
│   ├── db.py
│   ├── redis_client.py
│   └── migrations/
│
├── utils/
│   ├── password.py
│   ├── responses.py
│   ├── validators.py
│   └── decorators.py
│
├── config/
│   └── config.py
│
├── __init__.py
│
└── extensions.py


- comandos no terminal para visualizar projeto
* find app -type f
* ls app/services
* pip freeze requirements.txt