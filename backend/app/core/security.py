from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)


def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    time_delta = datetime.utcnow() + timedelta(minutes=15)
    if expire_delta:
        time_delta = datetime.utcnow() + expire_delta
    to_encode["exp"] = time_delta

    return jwt.encode(to_encode, settings.AUTH_SECRET_KEY, algorithm=settings.HASH_ALGHORITHM)
