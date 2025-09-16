from sqlalchemy import create_engine, text
import os

DB_USER = "spell_user"
DB_PASSWORD = "Sonofgod91!"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "spell_db"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1;"))
        print("Database connection successful:", result.scalar())
except Exception as e:
    print("Database connection failed:", e)
