from Models.ad_tags import ad_tags_association
from Models.ad import Ad
from Models.tag import Tag
from db.base import Base, Session, engine

Base.metadata.create_all(engine)

session = Session()

session.query(ad_tags_association).delete()
session.query(Tag).delete()
session.query(Ad).delete()

session.commit()
session.close()
