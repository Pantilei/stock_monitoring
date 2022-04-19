from app.db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Country(Base):
    name = Column(String, index=True)
    stocks = relationship("Stock", back_populates="country",
                          foreign_keys="Stock.country_id")
