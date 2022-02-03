import json
from fastapi.encoders import jsonable_encoder
from typing import Generic, TypeVar, Type, List, Union, Dict, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.base_class import Base


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemeType = TypeVar('CreateSchemeType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemeType, UpdateSchemaType]):
    """CRUD object with default methods for Create, Read, Update and Delte (CRUD)

    Args:
        Generic ([ModelType]): SQLAlchemy model class
        Generic ([CreateSchemeType]): Pydantic model class for create operation
        Generic ([UpdateSchemaType]): Pydantic model class for update operation
    """

    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def get(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, offset: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(offset).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemeType) -> ModelType:
        jsonable_data = jsonable_encoder(obj_in)
        db_obj = self.model(**jsonable_data)
        db.add(db_obj)
        db.flush()
        return db_obj

    def create_multi(self, db: Session, objs_in: List[CreateSchemeType]) -> List[ModelType]:
        db_objs = [self.model(**jsonable_encoder(obj_in))
                   for obj_in in objs_in]
        db.add_all(db_objs)
        db.flush()

        return db_objs

    def update(self, db: Session, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.flush()

        return db_obj

    def remove(self, db: Session, id: int) -> None:
        db_obj = db.query(self.model).get(id)
        db.delete(db_obj)
        db.flush()
