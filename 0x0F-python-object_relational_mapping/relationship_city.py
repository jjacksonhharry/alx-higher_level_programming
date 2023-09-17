#!/usr/bin/python3
"""
Contains the class definition of a City.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """City class."""
    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
