#!/usr/bin/python3

"""
State model class definition
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City (Base):
    """Represents city column in MySQL database.

    Attributes:
        __tablename__ (str): MySQL table name for cities.
        id (str): city instance id.
        name (sqlalchemy.Integer): city instance name.
        state_id (sqlalchemy.String): city's state instance id.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
