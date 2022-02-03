from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func


class User(Base):
    full_name = Column(String, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
