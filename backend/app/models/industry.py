from app.db.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Industry(Base):
    name = Column(String, index=True)
    sector_id = Column(Integer, ForeignKey("sector.id"))

    stocks = relationship("Stock", back_populates="industry",
                          foreign_keys="Stock.industry_id")
    sector = relationship(
        "Sector", back_populates="industry", foreign_keys="Sector.industry_id")
