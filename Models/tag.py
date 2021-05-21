from db.base import Base
from sqlalchemy import Column, Integer, String


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    value = Column('value', String(50))

    def __init__(self, value):
        self.value = value.lower()

    def __repr__(self):
        return {'id': self.id, 'value': self.value}

    def __str__(self):
        return f"{self.id}. {self.value}"
