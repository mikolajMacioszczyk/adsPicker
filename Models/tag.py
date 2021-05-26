from db.base import Base
from sqlalchemy import Column, Integer, String


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    value = Column('value', String(50))
    lang = Column('lang', String(3))

    def __init__(self, value, lang):
        self.value = value.lower()
        self.lang = lang

    def __repr__(self):
        return {'id': self.id, 'value': self.value, 'lang': self.lang}

    def __str__(self):
        return f"{self.id}. {self.value} - {self.lang}"
