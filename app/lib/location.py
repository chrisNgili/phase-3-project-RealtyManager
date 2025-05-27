from sqlalchemy.orm import sessionmaker
from models import Location


def create_location(session):
    city = input("Please Enter the City : ")
    neighbourhood = input("Please specify neighbourhood : ")

    location = Location(city = city, neighbourhood = neighbourhood)
    session.add(location)
    session.commit()

    print(f"{neighbourhood} of {city} created successfully ! ")

def list_locations(session):
    locations = session.query(Location).all()

    if not locations: print("Locations not found !")
    else:
        print("Location list :")
        for location in locations:
            print(f"ID: {location.id}, City: {location.city}, Neighbourhood: {location.neighbourhood}")