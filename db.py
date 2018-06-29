import datetime
import os
from sqlalchemy import create_engine, Column, Integer, Float, Unicode, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ.get("POSTGRES_URL"), echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Humidity(Base):
    
    __tablename__ = 'humidity'

    id = Column(Integer,
            Sequence('humidity_id_seq'), primary_key=True)
    value = Column(Float)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)