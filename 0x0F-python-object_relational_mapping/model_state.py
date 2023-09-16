#!/usr/bin/python3
"""
class definition of a State and an instance
Base = declarative_base()
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    states the class
    """
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True)
    name = Column(String(128), nullable=False)
