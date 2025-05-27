from models import PropertyType
from sqlalchemy.orm import sessionmaker

def create_property_type(session):
    type_name = input("Enter property type name : ")

    type = PropertyType(type_name = type_name)
    session.add(type)
    session.commit()

def list_property_types(session):
    property_types = session.query(PropertyType).all()

    if not property_types: print("No types found")
    else:
        print("Property types :")
        for types in property_types:
            print(f"ID : {types.id}, Type_name{types.type_name}")