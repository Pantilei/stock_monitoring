from venv import create
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import Token
from app.core.security import create_access_token

router = APIRouter()


@router.post("/login/access-token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {
        "access_token": create_access_token({
            "username": form_data.username,
            "scopes": form_data.scopes
        }),
        "token_type": "bearer"
    }
