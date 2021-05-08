from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@localhost:5432/asdPicker', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
Session = sessionmaker(bind=engine)
Base = declarative_base()