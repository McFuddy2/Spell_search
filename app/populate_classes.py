# populate_classes.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Class

# 1. Connect to your database
DB_URI = "postgresql+psycopg2://spell_user:Sonofgod91!@localhost:5432/spell_db"
engine = create_engine(DB_URI)


# 2. Create a session
Session = sessionmaker(bind=engine)
session = Session()

def populate_table(session, model_class, data_list, unique_field=None):
    """
    Generic function to populate a table.

    :param session: SQLAlchemy session
    :param model_class: SQLAlchemy model class (e.g., School)
    :param data_list: List of dictionaries with data to insert
    :param unique_field: Field name to check for duplicates (optional)
    """
    for data in data_list:
        if unique_field:
            exists = session.query(model_class).filter(
                getattr(model_class, unique_field) == data[unique_field]
            ).first()
            if exists:
                continue  # skip duplicates

        session.add(model_class(**data))

    session.commit()
    print(f"{model_class.__name__} table populated successfully!")


# 3. Example usage: populate Classes
classes_data = [
    {"name": "Artificer"},
    {"name": "Barbarian"},
    {"name": "Bard"},
    {"name": "Cleric"},
    {"name": "Druid"},
    {"name": "Fighter"},
    {"name": "Monk"},
    {"name": "Paladin"},
    {"name": "Ranger"},
    {"name": "Rogue"},
    {"name": "Sorcerer"},
    {"name": "Warlock"},
    {"name": "Wizard"},
]

populate_table(session, Class, classes_data, unique_field="name")

# Close the session when done
session.close()


