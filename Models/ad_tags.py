from sqlalchemy import Column, Integer, Table, ForeignKey
from db.base import Base


ad_tags_association = Table('ad_tags', Base.metadata,
                            Column('ad_id', Integer, ForeignKey('ads.id')),
                            Column('tag_id', Integer, ForeignKey('tags.id')))
