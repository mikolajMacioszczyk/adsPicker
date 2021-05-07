from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


ad_tags_association = Table('ad_tags', Base.metadata,
                            Column('ad_id', Integer, ForeignKey('ads.id')),
                            Column('tag_id', Integer, ForeignKey('tags.id')))


class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(128))
    description = Column('description', String(1024))
    imagePath = Column('imagePath', String(128))
    tags = relationship("Tag", secondary=ad_tags_association)

    def __init__(self, title, description, imagePath, tags=[]):
        self.title = title
        self.description = description
        self.imagePath = imagePath
        for tag in tags:
            tag.use()
        self.tags = tags

    @classmethod
    def default(cls):
        return Ad('title', 'description', 'path', ['tag'])

    def adTag(self, tag):
        if tag not in self.tags:
            tag.use()
            self.tags.append(tag)

    def update(self, updated):
        self.title = updated.title
        self.description = updated.description
        self.imagePath = updated.imagePath
        for tag in self.tags:
            tag.unUse()
        for tag in updated.tags:
            tag.use()
        self.tags = updated.tags

    def __str__(self):
        return f"{self.id}. {self.title} {self.description} {self.imagePath} tags: {', '.join([t.value for t in self.tags])}"


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

