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

* flask db init => inicializa as migrations
* flask db migrate -m "create users table"  =>gerar a migration
* flask db upgrade => aplicar a migration



# 🚀 Flask JWT Authentication API

API REST desenvolvida com Flask utilizando autenticação baseada em JWT, Refresh Token, SQLite, Redis e arquitetura modular.

## 📌 Objetivo

Fornecer uma estrutura profissional para autenticação e autorização de usuários, servindo como base para sistemas web, aplicações mobile, ERPs, painéis administrativos e microsserviços.

---

# 🏗 Arquitetura

```text
app/
│
├── routes/        # Endpoints da API
├── middleware/    # Segurança e validações
├── services/      # Regras de negócio
├── schemas/       # Validação dos dados
├── models/        # Entidades do banco
├── database/      # Conexões e persistência
├── utils/         # Funções auxiliares
├── config/        # Configurações da aplicação
│
├── __init__.py
└── extensions.py

run.py
```

---

# 🔄 Fluxo da Aplicação

## 1️⃣ Cadastro de Usuário

```http
POST /auth/register
```

Fluxo:

```text
Request
 ↓
Schema Validation
 ↓
Auth Service
 ↓
User Model
 ↓
SQLite Database
```

Resultado:

```json
{
    "success": true,
    "message": "Usuário criado com sucesso"
}
```

---

## 2️⃣ Login

```http
POST /auth/login
```

Fluxo:

```text
Request
 ↓
Validação
 ↓
Verificação de Senha
 ↓
Geração JWT
 ↓
Geração Refresh Token
 ↓
Redis
```

Resultado:

```json
{
    "access_token": "...",
    "refresh_token": "..."
}
```

---

## 3️⃣ Acesso a Rotas Privadas

```http
GET /user/profile
```

Header:

```http
Authorization: Bearer TOKEN
```

Fluxo:

```text
Request
 ↓
JWT Middleware
 ↓
Validação do Token
 ↓
Busca Usuário
 ↓
Resposta
```

---

## 4️⃣ Renovação de Token

```http
POST /auth/refresh
```

Fluxo:

```text
Refresh Token
 ↓
Redis
 ↓
Validação
 ↓
Novo Access Token
```

---

# 🔐 Recursos Implementados

* Autenticação JWT
* Refresh Token
* Hash de Senha
* Middleware de Segurança
* Validação com Marshmallow
* SQLAlchemy ORM
* SQLite
* Redis
* Arquitetura Modular
* API REST

---

# 🛠 Tecnologias Utilizadas

* Python
* Flask
* Flask-JWT-Extended
* SQLAlchemy
* Marshmallow
* SQLite
* Redis
* Flask-Migrate
* Python-Dotenv

---

# ▶️ Execução

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar aplicação:

```bash
python run.py
```

Health Check:

```http
GET /health/
```

---

# 📚 Finalidade Educacional

Este projeto demonstra a implementação completa de autenticação moderna utilizando JWT, Refresh Token e arquitetura em camadas, seguindo boas práticas de organização e separação de responsabilidades em aplicações Flask.
