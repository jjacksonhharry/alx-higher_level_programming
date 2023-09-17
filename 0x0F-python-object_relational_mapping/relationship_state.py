#!/usr/bin/python3
"""
Contains the class definition of a State.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class."""
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            back_populates="state",
            cascade="all, delete-orphan")
