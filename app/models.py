
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from base import Base ,engine

class Employee(Base):

    __tablename__ = 'employee'
    id = Column(Integer, primary_key = True)

    username = Column(String(20))
    password = Column(String(20))
    name = Column(String(20))
    email = Column(String(50))

def __init__(self, username, password, name, email):
    self.username = username
    self.password = password
    self.name = name
    self.email = email



Base.metadata.create_all(engine)