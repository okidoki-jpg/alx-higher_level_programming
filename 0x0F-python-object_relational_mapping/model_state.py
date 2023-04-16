#!/usr/bin/python3

"""
State model class definition
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State (Base):

    """Represents State column in MySQL database.

    Attributes:
        __tablename__ (str): MySQL table name for States.
        id (sqlalchemy.Integer): State instance id.
        name (sqlalchemy.String): State instance name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
