from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.cli import cli_functions


engine  = create_engine("sqlite:///RealtyManager.db", echo = False)
Session = sessionmaker(bind = engine)

session = Session()

def main():
        cli_functions(session)
main()