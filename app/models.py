from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Agent(Base):
    __tablename__ = "Agent"

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(), nullable=False, unique=True)
    # specialization_id = 
    pass

class Property(Base):
    __tablename__ = "Property"

    id = Column(Integer, primary_key= True)
    price = Column(Integer, nullable = False)
    description = Column(String(), nullable = False)
    rooms = Column(Integer, nullable = False)
    # type_id = 
    # agent_id = 
    # location_id = 
    pass

class Property_type(Base):
    __tablename__ = "Property_type"

    id = Column(Integer, primary_key = True)
    # type_name = 
    pass

class Location(Base):
    __tablename__ = "Location"

    id = Column(Integer, primary_key = True)
    city = Column(String(), nullable = False)
    pass

class Agent_specialization(Base):
    __tablename__ = "Agent_specialization"

    id = Column(Integer, primary_key = True)
    name = Column(String(), nullable = False)
    pass