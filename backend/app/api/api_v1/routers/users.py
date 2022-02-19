from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.api import deps
from sqlalchemy.orm import Session
from app import schemas, models, crud
from typing import List, Any
import json

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
async def get_users(
    response: Response,
    db: Session = Depends(deps.get_db),
    sort: str = json.dumps(["created_at", "desc"]),
    range: str = json.dumps([0, 100]),
    filter: str = json.dumps({}),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> List[schemas.User]:
    """
    Retreive list of users
    """
    sort_parsed = json.loads(sort)
    range_parsed = json.loads(range)
    filter_parsed = json.loads(filter)
    response.headers["content-range"] = f"users {range_parsed[0]}-{range_parsed[1]}/" + str(
        crud.user.get_count(db))
    return crud.user.get_multi_ordered(db, offset=range_parsed[0], limit=range_parsed[1], order_by=sort_parsed)


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
