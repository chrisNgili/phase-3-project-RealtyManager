from sqlalchemy.orm import sessionmaker
from models import Agent, Property, PropertyType, Location


def create_property(session):
    price = int(input("Enter property price: "))
    description = input("Enter property description: ")
    rooms = int(input("Enter number of rooms: "))

    property_types = session.query(PropertyType).all()
    print("Available property types:")
    for property_type in property_types:
        print(f"{property_type.id}. {property_type.type_name}")

    while True:
        try:
            type_id = int(input("Enter property type ID: "))
            if any(pt.id == type_id for pt in property_types):
                break
            else:
                print("Invalid property type ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    agents = session.query(Agent).all()
    print("Available agents:")
    for agent in agents:
        print(f"{agent.id}. {agent.name}")

    while True:
        try:
            agent_id = int(input("Enter agent ID: "))
            if any(a.id == agent_id for a in agents):
                break
            else:
                print("Invalid agent ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    locations = session.query(Location).all()
    print("Available locations:")
    for location in locations:
        print(f"{location.id}. {location.city}")

    while True:
        try:
            location_id = int(input("Enter location ID: "))
            if any(l.id == location_id for l in locations):
                break
            else:
                print("Invalid location ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
            
    property = Property(price=price, description=description, rooms=rooms, 
                        type_id=type_id, agent_id=agent_id, location_id=location_id)
    session.add(property)
    session.commit()

def list_properties(session):
    properties = session.query(Property).all()

    if not properties: print("No properties found")
    else:
        print("List of Properties :")
        for property in properties:
            print(f"ID: {property.id}, Price: {property.price}, Description: {property.description}, Rooms: {property.rooms}, Type ID: {property.type_id}, Agent ID: {property.agent_id}, Location ID: {property.location_id}")