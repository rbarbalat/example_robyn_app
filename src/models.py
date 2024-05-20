# models.py
from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./gotham_database.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


class Crime(Base):
    __tablename__ = "crimes"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    #suspect_name = Column(String)
    date = Column(DateTime, default = datetime.now())
    latitude = Column(Float)
    longitude = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "description": self.description,
            "location": self.location,
            "date": self.date,
            "latitude": self.latitude,
            "longitude": self.longitude
        }


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, hashed_password={self.hashed_password})>"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
