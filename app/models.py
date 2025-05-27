from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(), nullable=False, unique=True)
    specialization_id = Column(Integer, ForeignKey("agent_specializations.id"), nullable = False)

    properties = relationship("Property", back_populates="agent")
    specialization = relationship("AgentSpecialization", back_populates="agents")
    pass

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key= True)
    price = Column(Integer, nullable = False)
    description = Column(Text, nullable = False)
    rooms = Column(Integer, nullable = False)
    type_id = Column(Integer, ForeignKey("property_types.id"), nullable = False)
    agent_id = Column(Integer, ForeignKey("agents.id"), nullable = False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable = False)

    agent = relationship("Agent", back_populates="properties")
    property_type = relationship("PropertyType", back_populates="properties")
    location = relationship("Location", back_populates="properties")

    pass

class PropertyType(Base):
    __tablename__ = "property_types"

    id = Column(Integer, primary_key = True)
    type_name = Column(String(), nullable = False)

    properties = relationship("Property", back_populates="property_type")
    pass

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key = True)
    city = Column(String(), nullable = False)
    neighbourhood = Column(String(), nullable = False)

    properties = relationship("Property", back_populates="location")
    pass

class AgentSpecialization(Base):
    __tablename__ = "agent_specializations"

    id = Column(Integer, primary_key = True)
    name = Column(String(), nullable = False)

    agents = relationship("Agent", back_populates="specialization")
    pass