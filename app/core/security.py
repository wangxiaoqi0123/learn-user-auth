
import bcrypt
from datetime import datetime,timedelta,timezone

import jwt
from app.core.config import settings


# ── 密码加密及校验 ──────────────────────────────────────

def hash_password(password:str):
    return bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

def verify_password(password:str, hashed_password:str):
    return bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8'))


# ── jwt tokens ────────────────────────────────────────

def create_access_token(data:dict)->str:
    '''
    创建一个短期token，必须要有 sub 唯一id
    '''
    now = datetime.now(timezone.utc)
    payload = {
        **data,
        'sub':str(data['sub']),
        'exp':now + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS),
        'iat':now,
        'type':'sucess'
    }
    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
