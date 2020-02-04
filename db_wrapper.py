from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///bot.db', echo=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Voice(Base):
    __tablename__ = 'voice'
    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    path = Column(String)
    user = relationship("User")


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    path = Column(String)
    user = relationship("User")


def get_or_create_user(session, user_id, username):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        return user
    else:
        user = User(id=user_id, name=username)
        session.add(user)
        return user

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
