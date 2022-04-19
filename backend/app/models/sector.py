from app.db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Sector(Base):
    name = Column(String, index=True)
    stocks = relationship("Stock", back_populates="sector",
                          foreign_keys="Stocks.sector_id")
    industries = relationship(
        "Industry", back_populates="sector", foreign_keys="Industry.sector_id")
