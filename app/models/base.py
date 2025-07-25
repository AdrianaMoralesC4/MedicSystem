from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative, declared_attr

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)