from sqlalchemy.orm import sessionmaker
from models import Agent, AgentSpecialization

def create_agent(session):
    agent_name = input("Enter your name : ")
    agent_email = input("Enter your email : ")

    specializations = session.query(AgentSpecialization).all()
    print("Available specializations : ")
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

def update_agent(session):
    agent_id = int(input("Enter agent ID to update : "))
    agent = session.query(Agent).filter_by(id=agent_id).first()

    if agent:
        name = input("Enter new name: ")
        email = input("Enter new email : ")
        specialization_id = input("Enter new Specialization ID : ")
        if name: agent.name = name
        if email: agent.email = email
        if specialization_id: agent.specialization_id = specialization_id

        session.commit()
        print("Agent Update successfully 🎊🎊 !!")
    else: print("Agent not found!")

def delete_agent(session):
    agent_id = int(input("Enter agent ID to delete : "))
    agent = session.query(Agent).filter_by(id=agent_id).first()

    if agent:
        session.delete(agent)
        session.commit()
        print("Agent deleted successfully ! ")
    else: print("Agent not found")