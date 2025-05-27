from .agents import create_agent, list_agents, update_agent, delete_agent
from .property import create_property, list_properties, update_property, delete_property
from .location import create_location, list_locations, edit_location, delete_location
from .property_type import create_property_type, list_property_types
from .agent_specialization import create_agent_specialization
import sys





def cli_functions(session):
    while True:
        print("====================REALTY MANAGER====================")
        print("1. Manage Agents")
        print("2. Manage Properties")
        print("3. Manage Locations")
        print("0. Exit")
        main_choice = input("Enter Your Selection : ")

        if main_choice == "1":
            while True:
                print("\n========== Agents Management ==========")
                print("1. Create Agent")
                print("2. Create Agent Specialization")
                print("3. Update Agents")
                print("4. List Agents")
                print("5. Delete Agent")
                print("0. Return")

                choice = input("Enter Choice: ")
                if choice == "1":
                    create_agent(session)
                elif choice == "2":
                    create_agent_specialization(session)
                elif choice == "3":
                    update_agent(session)
                elif choice == "4":
                    list_agents(session)
                elif choice == "5":
                    delete_agent(session)
                elif choice =="0":
                    break
                else: print("Invalid choice. Please try again!")

        elif main_choice == "2":
            while True:
                print("\n==========Property Management==========")
                print("1. Create Property")
                print("2. List Properties")
                print("3. Edit Property")
                print("4. Delete Property")
                print("5. Create Property type")
                print("6. List Property Types")
                print("0. Return")
                choice = input("Enter Choice: ")

                if choice == "1":
                    create_property(session)
                elif choice == "2":
                    list_properties(session)
                elif choice == "3":
                    update_property(session)
                elif choice == "4":
                    delete_property(session)
                elif choice == "5":
                    create_property_type(session)
                elif choice == "6":
                    list_property_types(session)
                elif choice == "0":
                    break
                
                else : print("Invalid choice. Please Try Again")

        elif main_choice == "3":
            while True:
                print("\n========== Location Manager ==========")
                print("1. Create Location")
                print("2. List Locations")
                print("3. Edit Location")
                print("4. Delete Location")
                print("0. Return")
                choice = input("Enter Choice: ")

                if choice == "1":
                    create_location(session)
                elif choice == "2":
                    list_locations(session)
                elif choice == "3":
                    edit_location(session)
                elif choice == "4":
                    delete_location(session)
                elif choice =="0":
                    break
                else: print("Invalid choice please try again")
                
        elif main_choice =="0": 
            print("Exiting Realty Manager. Kwaheri 👋 ") 
            sys.exit()
        else: print("Invalid choice please try again")
