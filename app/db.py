# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base class for all table models
Base = declarative_base()

# Replace these with your PostgreSQL credentials
DB_USER = "spell_user"
DB_PASSWORD = "Sonofgod91!"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "spell_db"

# Connection string
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the engine (talks to the database)
engine = create_engine(DATABASE_URL, echo=True)  # echo=True prints SQL statements

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a session
def get_session():
    return SessionLocal()
