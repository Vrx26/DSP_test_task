from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///bot.db', echo=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Voice(Base):
    __tablename__ = 'voice'
    id = Column(Integer, primary_key=True)
    path = Column(String)
    author_id = Column(String, ForeignKey(User.id))


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    path = Column(String)
    author_id = Column(String, ForeignKey(User.id))


Base.metadata.create_all(engine)
conn = engine.connect()