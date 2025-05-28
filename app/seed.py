from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Property, PropertyType, Agent, AgentSpecialization, Location
import random
from faker import Faker

engine = create_engine("sqlite:///RealtyManager.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()
descriptions = [
    "This property is located in a prime area.",
    "It features modern amenities and a spacious layout.",
    "The neighborhood is known for its vibrant community.",
    "Close to schools, parks, and shopping centers.",
    "Recently renovated with high-end finishes.",
    "Perfect for families and professionals alike.",
    "Offers stunning views and a peaceful environment.",
    "Easy access to public transportation and major highways.",
    "Ideal for those looking for a blend of comfort and convenience.",
    "A rare find in today's market."]

def seed_data(session):
    session.query(Property).delete()
    session.query(Agent).delete()
    session.query(AgentSpecialization).delete()
    session.query(PropertyType).delete()
    session.query(Location).delete()

    agent_specializations = [
        AgentSpecialization(name = "Residential"),
        AgentSpecialization(name = "Commercial"),
        AgentSpecialization(name = "Land"),
        AgentSpecialization(name = "Property Management")
    ]
    session.add_all(agent_specializations)
    
    property_types = [
        PropertyType(type_name = "Mansion"),
        PropertyType(type_name = "Bungalow"),
        PropertyType(type_name = "Apartment"),
        PropertyType(type_name = "Commercial Land"),
        PropertyType(type_name = "Bnb"),
    ]
    session.add_all(property_types)

    locations = [
        Location(city=fake.city(), neighbourhood = fake.street_name())
        for _ in range (5)
    ] 
    session.add_all(locations)

    agents = [
        Agent(name=fake.name(), email=fake.email(), specialization_id=fake.random_int(min=1, max=4))
        for _ in range(10)
    ]
    session.add_all(agents)

    properties = [
        Property(
            price=fake.random_int(min=100000, max=1000000000),
            description = " ".join(random.sample(descriptions, 1)),
            rooms=fake.random_int(min=1, max=20),
            type_id=fake.random_int(min=1, max=5),
            agent_id=fake.random_int(min=1, max=10),
            location_id=fake.random_int(min=1, max=5)
        ) 
        for _ in range(20)
    ]
    session.add_all(properties)
    session.commit()
    print("Seed Data created successfully!!")

seed_data(session)