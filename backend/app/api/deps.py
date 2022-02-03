from curses.ascii import HT
from pyexpat import model
from webbrowser import get
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from app.core.config import settings
from app import schemas, models, crud
from app.db.session import SessionLocal
from typing import Generator
from sqlalchemy.orm import Session

import logging
import traceback
_logger = logging.getLogger(__name__)


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
    try:
        payload = jwt.decode(token, settings.AUTH_SECRET_KEY,
                             algorithms=settings.HASH_ALGHORITHM)
        print(payload)
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as er:
        print(er)
        _logger.error(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Could not validate credentials")
    user = crud.user.get(db, token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user


def get_current_active_user(current_user: models.User = Depends(get_current_user)) -> models.User:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")

    return current_user


def get_current_active_superuser(current_user: models.User = Depends(get_current_user)) -> models.User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")

    return current_user
