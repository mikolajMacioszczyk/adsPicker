from Models.ad_tags import Ad, Tag, ad_tags_association
from db.base import Base, Session, engine

Base.metadata.create_all(engine)

session = Session()

session.query(ad_tags_association).delete()
session.query(Tag).delete()
session.query(Ad).delete()

session.commit()
session.close()
