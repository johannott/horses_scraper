from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

import tutorial.settings


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    #return create_engine(get_project_settings().get("CONNECTION_STRING"))
    return create_engine(URL(**tutorial.settings.DATABASE))


def create_table(engine):
    for _t in Base.metadata.tables:
        print(_t)
    Base.metadata.create_all(engine)


# Association Table for Many-to-Many relationship between Quote and Tag
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
# quote_tag = Table('quote_tag', Base.metadata,
#     Column('quote_id', Integer, ForeignKey('quote.id')),
#     Column('tag_id', Integer, ForeignKey('tag.id'))
# )


# class Going(Base):
#     __tablename__ = "going"

#     id = Column(Integer, primary_key=True)
#     track = Column('track', String(30))
#     going = Column('going', String(100))

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    track_name = Column('track_name', String(255))
    current_going = Column('current_going', String(255))

# class Quote(Base):
#     __tablename__ = "quote"

#     id = Column(Integer, primary_key=True)
#     quote_content = Column('quote_content', Text())
#     author_id = Column(Integer, ForeignKey('author.id'))  # Many quotes to one author
#     tags = relationship('Tag', secondary='quote_tag',
#         lazy='dynamic', backref="quote")  # M-to-M for quote and tag


# class Author(Base):
#     __tablename__ = "author"

#     id = Column(Integer, primary_key=True)
#     name = Column('name', String(50), unique=True)
#     birthday = Column('birthday', DateTime)
#     bornlocation = Column('bornlocation', String(150))
#     bio = Column('bio', Text())
#     quotes = relationship('Quote', backref='author')  # One author to many Quotes


# class Tag(Base):
#     __tablename__ = "tag"

#     id = Column(Integer, primary_key=True)
#     name = Column('name', String(30), unique=True)
#     quotes = relationship('Quote', secondary='quote_tag',
#         lazy='dynamic', backref="tag")  # M-to-M for quote and tag