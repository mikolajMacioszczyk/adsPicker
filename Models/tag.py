from db.base import Base
from sqlalchemy import Column, Integer, String


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    useCount = Column(Integer)
    value = Column('value', String(50))

    def __init__(self, value):
        self.value = value
        self.useCount = 0

    def use(self):
        self.useCount += 1

    def unUse(self):
        self.useCount -= 1

    def __str__(self):
        return f"{self.id}. {self.value}"