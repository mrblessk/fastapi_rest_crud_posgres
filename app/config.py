# db engine
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# from file parse tools
import configparser

# Use configparser for get Postgres access data
config = configparser.ConfigParser()
config.read('..\config.ini', encoding='utf-8')

DB_ENGINE=config.get('PostgresSQL', 'DB_ENGINE')
DB_NAME=config.get('PostgresSQL', 'DB_NAME')
DB_USER=config.get('PostgresSQL', 'DB_USER')
DB_PASSWORD=config.get('PostgresSQL', 'DB_PASSWORD')
DB_HOST=config.get('PostgresSQL', 'DB_HOST')
DB_PORT=config.get('PostgresSQL', 'DB_PORT')

# Set db Url for sqlalchemy
DATABASE_URL = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL)

# Set db-session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# set Base model
Base = declarative_base()
