from db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.ad_tags import ad_tags_association, hidden_ad_tags_association
from Models.tag import Tag


class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(128))
    description = Column('description', String(1024))
    imagePath = Column('imagePath', String(128))
    tags = relationship("Tag", secondary=ad_tags_association)
    hiddenTags = relationship("Tag", secondary=hidden_ad_tags_association)

    def __init__(self, title, description, imagePath, tags, hiddenTags):
        self.title = title
        self.description = description
        self.imagePath = imagePath
        self.tags = self._assignNotNone(tags)
        self.hiddenTags = self._assignNotNone(hiddenTags)

    @staticmethod
    def _assignNotNone(tags):
        if tags is None:
            return []
        else:
            return tags

    @classmethod
    def default(cls):
        return Ad('title', 'description', 'path', [Tag('tag', 'en')], [Tag('tag', 'en')])

    def update(self, updated):
        self.title = updated.title
        self.description = updated.description
        self.imagePath = updated.imagePath
        self.tags = updated.tags
        self.hiddenTags = updated.hiddenTags

    def __repr__(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'imagePath': self.imagePath, 'tags': [tag.__repr__() for tag in self.tags]}

    def __str__(self):
        return f"{self.id}. {self.title} {self.description} {self.imagePath} tags: {', '.join([t.value for t in self.tags])}"