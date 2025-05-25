from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Agent(Base):
    __tablename__ = "Agent"

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(), nullalbe=False, unique=True)
    specialization_id = 
    pass

class Property(Base):
    pass

class Property_type(Base):
    pass

class Location(Base):
    pass

class Agent_specialization(Base):
    pass