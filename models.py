
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from database import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    theme_color = Column(String)

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id"))

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    position = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    player_id = Column(Integer, nullable=True)

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    opponent = Column(String)
    stats = Column(JSON, default={})
