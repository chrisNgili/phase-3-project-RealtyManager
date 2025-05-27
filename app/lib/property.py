from sqlalchemy.orm import sessionmaker
from models import Agent, Property, PropertyType, Location


def create_property(session):
    price = int(input("Enter property price: "))
    description = input("Enter property description: ")
    rooms = int(input("Enter number of rooms: "))

    agents = session.query(Agent).all()
    print("Which agent are you :")
    for agent in agents:
        print(f"{agent.id}. {agent.name}")
    agent_id = int(input("Enter agent ID: "))

    property_types = session.query(PropertyType).all()
    print("Which property type is this :")
    for property_type in property_types:
        print(f"{property_type.id}. {property_type.type_name}")
    type_id = int(input("Enter property type ID: "))

    locations = session.query(Location).all()
    print("Where is it located? :")
    for location in locations:
        print(f"{location.id}. {location.city} - {location.neighbourhood}")
    location_id = int(input("Enter location ID: "))

    property = Property(
        price=price,
        description=description,
        rooms=rooms,
        type_id=type_id,
        agent_id=agent_id,
        location_id=location_id
    )
    session.add(property)
    session.commit()
    print("Property created successfully! :)")

def list_properties(session):
    properties = session.query(Property).all()

    if not properties: print("No properties found")
    else:
        print("List of Properties :")
        for prop in properties:
            print(f"ID: {prop.id}, Price: {prop.price}, Description: {prop.description}, Rooms: {prop.rooms}, Type ID: {prop.type_id}, Agent ID: {prop.agent_id}, Location ID: {prop.location_id}")

def update_property(session):
    property_id = int(input("Enter property ID to update : "))
    property = session.query(Property).filter_by(id=property_id).first()

    if property:
        price = input("Enter new price : ")
        rooms = input("Enter new number of rooms : ")
        description = input("Enter new description : ")

        if price: property.price = price
        if rooms: property.rooms = rooms
        if description: property.description = description

        session.commit()
        print("Property updated successfully !!")
    else:print("Property not found!")

def delete_property(session):
    property_id = int(input("Enter property ID to delete : "))
    property = session.query(Property).filter_by(id=property_id).first()

    if property:
        session.delete(property)
        session.commit()
        print("Property deleted successfully! ")
    else: print("Property not found")