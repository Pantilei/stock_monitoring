from app.crud.base import CRUDBase
from app.schemas.users import UserCreate, UserUpdate
from app.models.users import User
from typing import Optional, Union
from sqlalchemy.orm import Session
from app.core.security import verify_password, get_password_hash


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser
        )
        db.add(db_obj)
        db.flush()

        return db_obj

    def update(self, db: Session, db_obj: User, obj_in: Union[UserUpdate, dict]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password", None):
            update_data["hashed_password"] = get_password_hash(
                update_data["password"])
            del update_data["password"]

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None

        return user


user = CRUDUser(User)
