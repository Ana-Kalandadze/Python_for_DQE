from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    news_type = Column(String)
    text = Column(String)
    city = Column(String)
    date = Column(Date)

class PrivateAd(Base):
    __tablename__ = 'private_ad'

    id = Column(Integer, primary_key=True)
    news_type = Column(String)
    text = Column(String)
    date = Column(Date)

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    news_type = Column(String)
    text = Column(String)
    temperature = Column(Integer)
    comment = Column(String)

# Replace following line with your DB
engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_no_duplicate(session, model, filter_dict, insert_dict):
    # Check for existing record
    if not session.query(model).filter_by(**filter_dict).first():
        # If no existing record is found, create and add new one
        new_record = model(**insert_dict)
        session.add(new_record)
        session.commit()

