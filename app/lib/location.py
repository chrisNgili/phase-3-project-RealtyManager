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

def edit_location(session):
    location_id = int(input("Enter location ID to edit : "))
    location = session.query(Location).filter_by(id=location_id).first()

    if location:
        city = input("Enter new City: ")
        neighbourhood = input("Enter new Neighbourhood : ")
        if city: location.city = city
        if neighbourhood: location.neighbourhood = neighbourhood

        session.commit()
        print("Location Updated successfully!! ")
    else: print("Location not found! ")

def delete_location(session):
    location_id = int(input("Enter location ID to delete : "))
    location = session.query(Location).filter_by(id=location_id).first()

    if location:
        session.delete(location)
        session.commit()
        print("Location Deleted successfully !! ")
    else: print("Location not found")