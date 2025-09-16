from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Date, Table, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class School(Base):
    __tablename__ = "schools"

    school_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    abbreviation = Column(String)


class Spell(Base):
    __tablename__ = "spells"

    spell_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    level = Column(Integer, nullable=False)

    school_id = Column(Integer, ForeignKey("schools.school_id"), nullable=False)
    casting_time_id = Column(Integer, ForeignKey("casting_times.casting_time_id"), nullable=False)
    range_id = Column(Integer, ForeignKey("ranges.range_id"), nullable=False)
    duration_id = Column(Integer, ForeignKey("durations.duration_id"), nullable=False)
    components_id = Column(Integer, ForeignKey("components.components_id"), nullable=False)
    source_id = Column(Integer, ForeignKey("sources.source_id"), nullable=False)

    ritual = Column(Boolean, default=False, nullable=False)
    is_current = Column(Boolean, default=True, nullable=False)

    school = relationship("School", backref="spells")

    targets = relationship("Target", secondary="spells_targets", back_populates="spells")
    tags = relationship("Spell_Tag", secondary="spells_and_spell_tags", back_populates="spells")

    __table_args__ = (
        UniqueConstraint('name', 'source_id', name='uq_spell_name_source_version'),
    )

class Target(Base):
    __tablename__ = "targets"

    target_id = Column(Integer, primary_key=True)
    target_name = Column(String, nullable=False)
    description = Column(Text)
    max_targets = Column(Integer) # For AOE calculate the max amount of spaces it can hit.
    size = Column(String)  # 1, 20, 30, 60, etc
    measurement = Column(String)  # feet, individuals
    shape = Column(String)  # individual, radius, cone, line, cube, sphere, etc

    spells = relationship("Spell", secondary="spells_targets", back_populates="targets")

class Class(Base):
    __tablename__ = "classes"

    class_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
class Spell_Target(Base):
    __tablename__ = "spells_targets"

    spell_id = Column(Integer,  ForeignKey("spells.spell_id"))
    target_id = Column(Integer, ForeignKey("targets.target_id"))

    __table_args__ = (
        PrimaryKeyConstraint('spell_id', 'target_id'),
    )

class Casting_Time(Base):
    __tablename__ = "casting_times"

    casting_time_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    unit = Column(String)
    special_description = Column(String)
    
class Range(Base):
    __tablename__ = "ranges"

    range_id = Column(Integer, primary_key=True)
    range_type = Column(String)
    distance = Column(Integer)
    unit = Column(String)
    

class Duration(Base):
    __tablename__ = "durations"

    duration_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    unit = Column(String)
    concentration = Column(Boolean, default=False)
    special_description = Column(String)
    

class Component(Base):
    __tablename__ = "components"

    components_id = Column(Integer, primary_key=True)
    vocal = Column(Boolean, default=False)
    somatic = Column(Boolean, default=False)
    material = Column(Boolean, default=False)
    material_text = Column(String)
    material_cost = Column(Integer)
    material_consumed = Column(Boolean, default=False)

class Source(Base):
    __tablename__ = "sources"

    source_id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    publish_date = Column(Date)
    source_type = Column(String)
    
class Spell_Tag(Base):
    __tablename__ = "spell_tags"

    tag_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    spells = relationship("Spell", secondary="spells_and_spell_tags", back_populates="tags")
    
class Spell_and_Spell_Tag(Base):
    __tablename__ = "spells_and_spell_tags"

    spell_id = Column(Integer,  ForeignKey("spells.spell_id"))
    tag_id = Column(Integer, ForeignKey("spell_tags.tag_id"))

    __table_args__ = (
        PrimaryKeyConstraint('spell_id', 'tag_id'),
    )
    