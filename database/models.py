from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Base(DeclarativeBase):
  pass 


class User(Base):
  __tablename__ = "users"
  id = Column(
    Integer,
    primary_key= True
  )
  name = Column(String)
  age = Column(Integer)