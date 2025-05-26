from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Agent, Property, Location, Agent_specialization, Property_type, Base

engine  = create_engine("sqlite:///RealtyManager.db", echo = False)
Session = sessionmaker(bind = engine)

session = Session()




#AGENT:

def create_agent():
    input
# session.add()
# session.commit