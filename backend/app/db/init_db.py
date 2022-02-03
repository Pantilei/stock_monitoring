from app import crud, schemas
from app.core.config import settings
from sqlalchemy.orm import Session


def init_db(db: Session):
    user_in = schemas.UserCreate(
        email=settings.FIRST_SUPERUSER,
        password=settings.FIRST_SUPERUSER_PASSWORD,
        active=True,
        is_superuser=True
    )

    user = crud.user.get_by_email(db, user_in.email)
    if not user:
        crud.user.create(db, user_in)
