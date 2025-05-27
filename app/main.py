from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

from lib.agents import create_agent, list_agents
from lib.property import create_property, list_properties
from lib.location import create_location, list_locations
from lib.property_type import create_property_type, list_property_types
from lib.agent_specialization import create_agent_specialization, list_agent_specializations

engine  = create_engine("sqlite:///RealtyManager.db", echo = False)
Session = sessionmaker(bind = engine)

session = Session()



def main():
    while True:
        print("====================REALTY MANAGER====================")
        print("1. Create Agent")
        print("2. Create Property")
        print("3. Create Location")
        print("4. Create Property Type")
        print("5. Create Agent Specialization")
        print("6. List Agents")
        print("7. List Properties")
        print("8. List Locations")
        print("9. List Property Types")
        print("10. List Agent Specializations")
        print("11. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_agent(session)
        elif choice == "2":
            create_property(session)
        elif choice == "3":
            create_location(session)
        elif choice == "4":
            create_property_type(session)
        elif choice == "5":
            create_agent_specialization(session)
        elif choice == "6":
            list_agents(session)
        elif choice == "7":
            list_properties(session)
        elif choice == "8":
            list_locations(session)
        elif choice == "9":
            list_property_types(session)
        elif choice == "10":
            list_agent_specializations(session)
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__': main()