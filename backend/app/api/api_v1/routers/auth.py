from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app import schemas
from app.core import security
from app.api.deps import get_db
from app import crud
from sqlalchemy.orm import Session
from app.core.config import settings
from datetime import timedelta

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """Get OAuth2 compatible token

    Args:
        db (Session, optional): database session object. Defaults to Depends(get_db).
        form_data (OAuth2PasswordRequestForm, optional): Form data. Defaults to Depends().

    Returns:
        Token: Dictionary with token data
    """
    user = crud.user.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User inactive")
    access_token_expire_time = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_TIME)
    print("access_token_expire_time", access_token_expire_time)
    return {
        "access_token": security.create_access_token(data={
            "sub": str(user.id),
            "scopes": "admin" if user.is_superuser else "user"
        }, expire_delta=access_token_expire_time),
        "token_type": "bearer"
    }
