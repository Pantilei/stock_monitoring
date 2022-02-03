from datetime import datetime
from typing import Any
import re
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import func, Column, DateTime, Integer

from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(utcnow, 'mssql')
def ms_utcnow(element, compiler, **kw):
    return "GETUTCDATE()"


@as_declarative()
class Base:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return "_".join([r.lower() for r in re.sub(r"([A-Z])", r" \1", cls.__name__).split()])

    @declared_attr
    def id(cls):
        col = Column(Integer, primary_key=True, index=True)
        col._creation_order = 1

        return col

    @declared_attr
    def updated_at(cls):
        col = Column(DateTime(timezone=False),
                     server_default=utcnow(), onupdate=utcnow())
        col._creation_order = 9999
        return col

    @declared_attr
    def created_at(cls):
        col = Column(DateTime(timezone=False), server_default=utcnow())
        col._creation_order = 10000
        return col
