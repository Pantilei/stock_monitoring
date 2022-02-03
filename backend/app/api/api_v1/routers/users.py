from fastapi import APIRouter, Depends, HTTPException, status
from app.api import deps
from sqlalchemy.orm import Session
from app import schemas, models, crud
from typing import List, Any

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
async def get_users(
    db: Session = Depends(deps.get_db),
    limit: int = 100,
    offset: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> List[schemas.User]:
    """
    Retreive list of users
    """
    return crud.user.get_multi(db, offset=offset, limit=limit)


@router.get('/{user_id}', response_model=schemas.User)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_active_user)
) -> schemas.User:
    user = crud.user.get(db, user_id)
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough privileges")

    return user


@router.post('/', response_model=schemas.User)
def create_user(
    user_in: schemas.UserCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> schemas.User:
    user = crud.user.get_by_email(db, user_in.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with provided email already exists")
    user = crud.user.create(db, obj_in=user_in)
    db.commit()

    return user


@router.put('/{user_id}', response_model=schemas.User)
def update_user(
    user_id: int,
    user_in: schemas.UserUpdate,
    db: Session = Depends(deps.get_db),
    curret_user: models.User = Depends(deps.get_current_active_user)
) -> schemas.User:
    user = crud.user.get(db, user_id)
    print("user: ", user)
    print()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    db.commit()

    return user
