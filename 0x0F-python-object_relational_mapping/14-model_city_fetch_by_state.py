#!/usr/bin/python3

"""
A script that connects to an SQL database via SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":

    args = sys.argv
    db = f"mysql+mysqldb://{args[1]}:{args[2]}@localhost/{args[3]}"

    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
