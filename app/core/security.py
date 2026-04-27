import bcrypt
from datetime import datetime, timedelta, timezone

import jwt
from app.core.config import settings
from app.core.exceptions import TokenExpiredError, TokenInvalidError


# ── 密码加密及校验 ──────────────────────────────────────


def hash_password(password: str):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


# ── jwt tokens ────────────────────────────────────────


def create_access_token(data: dict) -> str:
    """
    创建一个短期token，必须要有 sub 唯一id
    """
    now = datetime.now(timezone.utc)
    payload = {
        **data,
        "sub": str(data["sub"]),
        "exp": now + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS),
        "iat": now,
        "type": "sucess",
    }
    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def create_refresh_token(data: dict) -> str:
    """
    创建一个长期的token，必须且只需要有 sub 唯一id
    """
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(data["sub"]),
        "exp": now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        "iat": now,
        "type": "sucess",
    }
    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def verify_token(token: str) -> dict:
    """
    解码token
    """
    try:
        jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError()
    except jwt.InvalidTokenError:
        raise TokenInvalidError()
