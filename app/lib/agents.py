from sqlalchemy.orm import sessionmaker
from models import Agent, AgentSpecialization

def create_agent(session):
    agent_name = input("Enter your name : ")
    agent_email = input("Enter your email : ")

    specializations = session.query(AgentSpecialization).all()
    print("Available specialization : ")
    for specialization in specializations:
        print(f"{specialization.id}. {specialization.name}")

    while True:
        try:
            specialization_id = int(input("Enter specialization ID: "))
            if any(s.id == specialization_id for s in specializations):
                break
            else:
                print("Invalid specialization ID. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    user1 = Agent(name = agent_name, email = agent_email, specialization_id = specialization_id )
    session.add(user1)
    session.commit()
    print(agent_name, " created successfully! :)")


def list_agents(session):
    agents = session.query(Agent).all()

    if not agents: print("No agents found.")
    else:
        print("List of Agents: ")
        for agent in agents:
            print(f"ID: {agent.id}, Name: {agent.name}, Email: {agent.email}, Specialization ID :{agent.specialization_id}")
