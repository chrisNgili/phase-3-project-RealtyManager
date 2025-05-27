from sqlalchemy.orm import sessionmaker
from models import AgentSpecialization

def create_agent_specialization(session):
    speciality = input("Enter your field of specialization : ")

    specilization = AgentSpecialization(name = speciality)
    session.add(specilization)
    session.commit()
    print(f"Specialization '{speciality}' created successfully! :)")

def list_agent_specializations(session):
    specialization_list = session.query(AgentSpecialization).all()

    if not specialization_list:print("Specializations not found")
    else:
        print("Specialization list :")
        for specialization in specialization_list:
            print(f"ID: {specialization.id}, Name : {specialization.name}")

