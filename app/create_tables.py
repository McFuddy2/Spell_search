# app/create_tables.py
from sqlalchemy import create_engine
from app.models import Base

DATABASE_URL = "postgresql+psycopg2://spell_user:Sonofgod91!@localhost:5432/spell_db"
engine = create_engine(DATABASE_URL)

# This will create all tables defined in models.py
Base.metadata.create_all(engine)

print("All tables created successfully!")
